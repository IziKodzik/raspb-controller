import math
import sys
import threading
import time

import adafruit_adxl34x
import requests

from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
from threading import Thread, Event


class Robot:

    def count_shift(self):

        pass

    def count_wheel_ticks(self, decoder):
        print('Decoding...')
        current_thread = threading.currentThread()
        while not getattr(current_thread, "_stopped"):
            decoder.wait_for_change(not getattr(current_thread, "_stopped"))
            self.counted_ticks += 1
        print('Decoding ended.')

    def __init__(self):

        motor1 = Motor(21, 20, 16)
        motor2 = Motor(13, 19, 26)

        stepper = StepperMotor(17, 27)

        wheel_decoder = Decoder(23)

        i2c = busio.I2C(board.SCL, board.SDA)
        vl53 = adafruit_vl53l0x.VL53L0X(i2c)
        self.accelerometer = adafruit_adxl34x.ADXL345(i2c)
        self.acceleration = [0, 0, 0]
        self.x = 0.0
        y = 0.0

        points = []
        print('First scan.')
        for i in range(0, 1600):
            distance = vl53.range
            if distance > 8000:
                distance = 0

            if distance != 0:
                radians = i * 0.225 * math.pi / 180.0
                points.append({'x': (distance * math.sin(radians)), 'y': (distance * math.cos(radians))})
            stepper.take_step()

        stepper.change_dir()
        for i in range(0, 1600):
            stepper.take_step()

        stepper.change_dir()
        map_points_data = {'map-points': points}
        res = requests.post("http://192.168.0.115:8080/map-points", json=map_points_data)
        points.clear()
        self.counted_ticks = 0
        decoder_counter_thread = threading.Thread(target=self.count_wheel_ticks, args=(wheel_decoder,))
        decoder_counter_thread._stopped = False
        decoder_counter_thread.start()
        motor1.go_forward()
        motor2.go_forward()
        time.sleep(2)
        motor1.stop()
        motor2.stop()
        decoder_counter_thread._stopped = True
        time.sleep(0.5)
        self.x += self.counted_ticks * 5.4
        print('ticks')
        print(self.counted_ticks)
        print('xs')
        print(self.x)
        print('Second scan.')
        for i in range(0, 1600):
            distance = vl53.range
            if distance > 8000:
                distance = 0

            if distance != 0:
                radians = i * 0.225 * math.pi / 180.0
                points.append({'x': (distance * math.sin(radians)), 'y': (distance * math.cos(radians) + self.x)})

            stepper.take_step()
        stepper.change_dir()
        for i in range(0, 1600):
            stepper.take_step()
        stepper.change_dir()

        map_points_data = {'map-points': points}
        points.clear()
