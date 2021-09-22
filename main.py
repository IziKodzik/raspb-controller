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
    left_motor = Motor(16)
    while True:
        left_motor.pwm_pin.on()
        sleep(1)
        left_motor.pwm_pin.off()
        sleep(1)

