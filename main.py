import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
from Motor import Motor
import RPi.GPIO
from gpiozero import LED, PWMLED, DistanceSensor
from StepperMotor import StepperMotor

if __name__ == '__main__':
    print('controller running')
    pwm = LED(18)
    while True:
        pwm.value = 100
        pwm.on()
        sleep(1)
        pwm.value = 10
        pwm.on()
        sleep(1)
