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
    pwm = PWMLED(18)
    ain1 = LED(15)
    ain1.on()
    ain2 = LED(14)
    while True:
        for x in range(100):
            pwm.value = x/100.0
            sleep(0.01)
        ain1.toggle()
        ain2.toggle()



