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
    left_motor.pwm_pin.on()
    sleep(5)
    left_motor.pwm_pin.off()

