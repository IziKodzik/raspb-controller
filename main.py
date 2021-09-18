
import random
import sys
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
    while True:
        radar_motor.take_steps(200 * 8)
        l.on()
        print(sensor.distance)
