import os
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


def test(bo):
    print('Noted:')
    bo.turn_left()



if __name__ == '__main__':
    bot = prepare_robot()
    sensor = DistanceSensor(echo=24, trigger=23, pin_factory=PiGPIOFactory())
    sensor.threshold_distance = 0.7
    # sensor.when_in_range = partial(test, bot)
    while True:
        bot.go_forward()
        sensor.wait_for_in_range()
        bot.turn_left()
        sensor.wait_for_out_of_range()
