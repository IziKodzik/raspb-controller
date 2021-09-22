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
    left_motor = Motor(18)
    left_motor.pwm_pin.off()
    while True:
        for i in range(0, 100):
            left_motor.pwm_pin.value = i / 100.0
            sleep(0.01)
        sleep(1)
        for i in range(0, 100):
            left_motor.pwm_pin.value = (100 - i) / 100.0
            sleep(0.01)
