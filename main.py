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
    i = LED(23)
    j = LED(24)
    i.on()
    j.on()
    pwm.on()

    sleep(10)
