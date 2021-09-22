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
    left_motor = PWMLED(18)
    left_motor.off()
    while True:
        left_motor.value = random.randrange(0, 100) / 100.0
