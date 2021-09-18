

import random
import sys
from time import sleep
from datetime import datetime
from gpiozero import Button

from gpiozero import LED, Pin, Button, DigitalInputDevice
from StepperMotor import StepperMotor

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.g


if __name__ == '__main__':
    print_hi('PyCharm')
    radar_motor = StepperMotor(16)
    while True:
        radar_motor.take_step()
        sleep(0.1)


