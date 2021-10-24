import sys
from threading import Thread
from time import sleep
from gpiozero import DistanceSensor, LED

from Motor import Motor
from Robot import Robot
from functools import partial



def prepare_robot():
    right_motor = Motor(14, 15, 18)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


if __name__ == '__main__':
    led = LED(15)
    led.on()
    while True:
        1
