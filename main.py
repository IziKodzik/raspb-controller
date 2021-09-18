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
    pin = LED(16)
    while True:
        for no in range(200 * 8):
            pin.on()
            sleep(0.0001)
            pin.off()
            sleep(0.0001)
        sleep(1)
