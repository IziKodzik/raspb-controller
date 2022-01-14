import math
import sys
import threading
import time

import adafruit_adxl34x
import requests
import PIL.Image

from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
import numpy as np
from threading import Thread, Event
from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image


class Robot:

    def detect_shift(self):
        print('Detecting acceleration...')
        spin = 0
        current_thread = threading.currentThread()
        while not getattr(current_thread, "_stopped"):
            acceleration = self.accelerometer.acceleration
            if abs(acceleration[1]) > 0.25:
                self.velocity[1] = self.velocity[1] + acceleration[1] * 0.001
            if abs(acceleration[0]) > 0.25:
                self.velocity[0] = self.velocity[0] + acceleration[0] * 0.001
                sz = self.velocity[0] / 7.0
                spin += sz
            time.sleep(0.001)
            self.shift[1] = self.shift[1] + self.velocity[1] * 0.001 * math.cos(spin)
            self.shift[0] = self.shift[0] + self.velocity[1] * 0.001 * math.sin(spin)

        print(self.shift)
        print('Detecting acceleration ended.')

    def count_wheel_ticks(self, decoder):
        print('Decoding...')
        current_thread = threading.currentThread()
        while not getattr(current_thread, "_stopped"):
            decoder.wait_for_change(not getattr(current_thread, "_stopped"))
            self.counted_ticks += 1
        print('Decoding ended.')

    def display_image(self):
        print('xd')
        # rev.1 users set port=0
        # substitute spi(device=0, port=0) below if using that interface
        # substitute bitbang_6800(RS=7, E=8, PINS=[25,24,23,27]) below if using that interface
        serial = i2c(port=1, address=0x3C)

        # substitute ssd1331(...) or sh1106(...) below if using that device

        device = sh1106(serial)
        img_path = 'peppo happyL.jpg'
        img = Image.open(img_path).convert('RGBA')
        ffff = Image.new(img.mode, img.size, (255,) * 4)

        back = Image.new("RGBA", device.size, "white")
        posn = ((device.width - img.width) // 2, 0)
        rot = img.rotate(0, resample=Image.BILINEAR)
        img = Image.composite(rot, ffff, rot)
        back.paste(img, posn)
        device.display(back.convert(device.mode))

    def find_landmarks(self):
        stepper = StepperMotor(17, 27)
        i2c = busio.I2C(board.SCL, board.SDA)
        distance_sensor = adafruit_vl53l0x.VL53L0X(i2c)

        distances = []
        points = []
        landmarks = []

        distance = distance_sensor.distance
        distances.append(distance)

        radians = math.radians(0)
        point = {'x': math.sin(radians) * distance, 'y': math.cos(radians) * distance, 'scan_no': 0}
        points.append(point)

        stepper.take_step()

        ty = None

        for i in range(1, 1600):
            distance = distance_sensor.range

            distances.append(distance)

            radians = math.radians(i * 0.225)
            point = {'x': math.sin(radians) * distance, 'y': math.cos(radians) * distance, 'scan_no': 0}
            points.append(point)

            delta = distances[len(distances) - 2] - distances[len(distances) - 1]

            if delta > 20:
                landmarks.append(points[len(distances) - 2])
                ty = None
            elif delta < -20:
                landmarks.append(points[len(distances) - 2])
                ty = None
            else:
                if ty is None:
                    if distances[len(distances) - 2] > distances[len(distances) - 1]:
                        ty = 'D'
                    elif distances[len(distances) - 2] < distances[len(distances) - 1]:
                        ty = 'A'
                    elif distances[len(distances) - 2] == distances[len(distances) - 1]:
                        ty = 'S'

                elif ty == 'D':
                    if distances[len(distances) - 2] > distances[len(distances) - 1]:
                        pass
                    else:
                        if distances[len(distances) - 2] < distances[len(distances) - 1]:
                            ty = 'A'
                        elif distances[len(distances) - 2] == distances[len(distances) - 1]:
                            ty = 'S'
                        landmarks.append(points[len(distances) - 2])

                elif ty == 'A':
                    if distances[len(distances) - 2] < distances[len(distances) - 1]:
                        pass
                    else:
                        if distances[len(distances) - 2] > distances[len(distances) - 1]:
                            ty = 'D'
                        elif distances[len(distances) - 2] == distances[len(distances) - 1]:
                            ty = 'S'
                        landmarks.append(points[len(distances) - 2])

                elif ty == 'S':
                    if distances[len(distances) - 2] == distances[len(distances) - 1]:
                        pass
                    else:
                        if distances[len(distances) - 2] < distances[len(distances) - 1]:
                            ty = 'A'
                        elif distances[len(distances) - 2] > distances[len(distances) - 1]:
                            ty = 'D'
                        landmarks.append(points[len(distances) - 2])

                stepper.take_step()
                print(f"{distance}mm")
                print(landmarks)
        stepper.change_dir()
        for i in range(0, 1600):
            stepper.take_step()
        stepper.change_dir()
        print(landmarks)

    def decoders(self):

        dec1 = Decoder(23)
        dec2 = Decoder(24)
        dec1.wait_for_change()
        print(1)

    def __init__(self):
        self.display_image()
        self.decoders()
        print('ended')
        sys.exit(2137)
        while True:
            pass

        motor1 = Motor(21, 20, 16)
        motor2 = Motor(13, 19, 26)
        # motor1.go_forward()
        # motor2.go_backward()

        # wheel_decoder = Decoder(23)

        i2c = busio.I2C(board.SCL, board.SDA)
        vl53 = adafruit_vl53l0x.VL53L0X(i2c)
        self.accelerometer = adafruit_adxl34x.ADXL345(i2c)
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.shift = np.array([0.0, 0.0, 0.0])

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
        map_points_data = {'map-points': points, 'i': 0}
        res = requests.post("http://192.168.0.115:8080/map-points", json=map_points_data)
        points.clear()
        self.counted_ticks = 0
        decoder_counter_thread = threading.Thread(target=self.detect_shift)
        decoder_counter_thread._stopped = False
        decoder_counter_thread.start()
        motor1.go_forward()
        motor2.go_forward()
        time.sleep(2)
        motor1.stop()
        motor2.stop()
        decoder_counter_thread._stopped = True
        time.sleep(0.5)
        print(self.shift)
        for i in range(0, 1600):
            distance = vl53.range
            if distance > 8000:
                distance = 0

            if distance != 0:
                radians = i * 0.225 * math.pi / 180.0
                points.append({'x': (distance * math.sin(radians) - self.shift[0] * 10000),
                               'y': (distance * math.cos(radians)) - self.shift[1] * 10000})

            stepper.take_step()
        stepper.change_dir()
        for i in range(0, 1600):
            stepper.take_step()
        stepper.change_dir()

        map_points_data = {'map-points': points, 'i': 1}
        requests.post("http://192.168.0.115:8080/map-points", json=map_points_data)

        points.clear()
