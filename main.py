import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
from Motor import Motor
from gpiozero import PWMLED, DistanceSensor
from StepperMotor import StepperMotor

if __name__ == '__main__':
    print('controller running')
    left_motor = Motor(15)
    while True:
        left_motor.go_with_speed(0.3)
        sleep(1)
        left_motor.go_with_speed(1)
        sleep(1)

