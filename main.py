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
    left_motor = Motor(8)
    left_motor.go_with_speed(0.01)
    sleep(4)
    left_motor.pwm_pin.off()

