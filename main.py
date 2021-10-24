import sys
from threading import Thread
from time import sleep
from gpiozero import DistanceSensor, LED

from Motor import Motor
from Robot import Robot
from functools import partial
# 14 - yellow with black
# 15 - green
# 16 - black
# 17 - blue
# 27 - red
# 22 - yellow

def prepare_robot():
    right_motor = Motor(14, 15, 18)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


if __name__ == '__main__':
    bot = prepare_robot()
    bot.go_forward()
    while True:
        1
