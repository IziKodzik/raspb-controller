import datetime
import os
import sys
import time
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


def test(bo):
    print('Noted:')
    bo.turn_left()


if __name__ == '__main__':
    bot = prepare_robot()
    sensor = DistanceSensor(echo=24, trigger=23, pin_factory=PiGPIOFactory())
    sensor.threshold_distance = 0.7
    # sensor.when_in_range = partial(test, bot)
    end = time.time() + 10
    while time.time() < end:
        bot.go_forward()
        while sensor.distance > 0.5:
            1
        bot.turn_left()
        while sensor.distance < 0.5:
            1
