import random
import sys
from threading import Thread
from time import sleep
from datetime import datetime
from Motor import Motor
from gpiozero import LED, PWMLED, DistanceSensor
from StepperMotor import StepperMotor

if __name__ == '__main__':
    print('controller running')
    pwma = PWMLED(14)
    pwma.value = 0.5
    ao2 = LED(15)
    ao2.on()
    ao1 = LED(18)
    ao1.off()

