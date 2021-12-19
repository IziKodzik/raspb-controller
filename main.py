import math
import sys
import threading
import time

import requests

from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
from threading import Thread, Event

def d00pa():
    current_thread = threading.currentThread()
    while not getattr(current_thread, "_stopped"):
        print('dpa')


decoder_counter_thread = threading.Thread(target=nigg)
decoder_counter_thread._stopped = False
decoder_counter_thread.start()
time.sleep(4)
decoder_counter_thread._stopped = True

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
points = []

for i in range(0, 1600):
    distance = vl53.range
    if distance > 8000:
        distance = 0

    if distance != 0:
        radians = i * 0.225 * math.pi / 180.0
        points.append({'x': (distance * math.sin(radians)), 'y': (distance * math.cos(radians))})

    stepper.take_step()
thread._stopped = True
mapPointsData = {'map-points': points}
res = requests.post("http://192.168.0.115:8080/map-points", json=mapPointsData)
stepper.change_dir()

for i in range(0, 1600):
    stepper.take_step()

for point in points:
    print(f'{point["x"]},{point["y"]}')
