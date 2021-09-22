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
    while True:
        left_motor.on()
        sleep(1)
        left_motor.off()
        sleep(0.5)

