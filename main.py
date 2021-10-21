import sys
from threading import Thread
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor

from Motor import Motor
from Robot import Robot
from functools import partial


def test(proc):
    proc = False


def prepare_robot():
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


if __name__ == '__main__':
    proceed = True

    collision_sensor = DistanceSensor(echo=23, trigger=24, pin_factory=PiGPIOFactory())
    collision_sensor.threshold_distance = 0.05
    collision_sensor.when_deactivated = partial(test, proceed)
    while proceed:
        sleep(1)
        print(collision_sensor.distance)
