import math
import sys
import time

import requests

from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
from threading import Thread, Event

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
    radians = 0.225 * math.pi / 360.0
    points.append({'x': (distance * math.sin(radians)), 'y': (distance * math.sin(radians))})
    stepper.take_step()
    time.sleep(0.1)

mapPointsData = {'map-points': points}
res = requests.post("http://192.168.0.115:8080/map-points", json=mapPointsData)
stepper.change_dir()

for i in range(0, 1600):
    stepper.take_step()

for point in points:
    print(f'{point["x"]},{point["y"]}')
