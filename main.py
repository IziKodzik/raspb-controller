import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
from gpiozero import Button
from Motor import Motor
from gpiozero import LED, DistanceSensor
from StepperMotor import StepperMotor

if __name__ == '__main__':
    print('controller running')
    left_motor =LED(16)
    while True:
        left_motor.on()
        sleep(1)
        left_motor.off()
        sleep(1)

