import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
from gpiozero import Button

from gpiozero import LED, DistanceSensor
from StepperMotor import StepperMotor


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.g


if __name__ == '__main__':
    print_hi('Controller')
    sensor = DistanceSensor(echo=23, trigger=24)
    radar_motor = StepperMotor(14, 15)
    l = LED(18)
    sensor.threshold = 10 / 100
    while True:
        if sensor.distance < 0.1:
            l.on()
            print('???')
        else:
            l.off()