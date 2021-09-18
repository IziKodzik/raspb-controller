
import random
import sys
from time import sleep
from datetime import datetime
from gpiozero import Button

from gpiozero import LED, Pin, Button, DigitalInputDevice


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.g


if __name__ == '__main__':
    print_hi('PyCharm')
    ledW = LED(16)
    while True:
        sleep(1)
        ledW.toggle()


