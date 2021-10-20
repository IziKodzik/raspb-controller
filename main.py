import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
import pygame

import pygame.key

from Motor import Motor
from pygame.locals import *
import RPi.GPIO
from gpiozero import LED, PWMLED, DistanceSensor
from StepperMotor import StepperMotor

if __name__ == '__main__':
    print('controller running')
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    left_motor.toggle_direction()
    left_motor.go_with_speed(1)
    right_motor.go_with_speed(1)
    while True:
        xd = input("Enter")
