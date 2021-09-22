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
    l = LED(18)
    while True:
        l.on()
        sleep(0.25)
        l.off()
        sleep(0.25)
