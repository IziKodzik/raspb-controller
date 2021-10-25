import sys
from threading import Thread
from time import sleep
from gpiozero import DistanceSensor, LED

from Motor import Motor
from Robot import Robot
from gpiozero.pins.pigpio import PiGPIOFactory

from functools import partial


# 14 - yellow with black
# 15 - green
# 18 - black
# 17 - blue
# 27 - red
# 22 - yellow

def prepare_robot():
    right_motor = Motor(14, 15, 18)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


def tst():
    print("true")


def test():
    print("tre")


if __name__ == '__main__':
    bot = prepare_robot()
    print('?')
    sleep(2)
    sensor = DistanceSensor(echo=24, trigger=23, pin_factory=PiGPIOFactory())
    sensor.when_in_range = test
    sleep(100)
    print('??')
