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
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    left_motor.toggle_direction()

    while True:
        for x in range(100):
            right_motor.go_with_speed(x / 100.0)
            left_motor.go_with_speed(x / 100.0)
            sleep(0.1)
        sleep(0.3)

        for x in range(100):
            right_motor.go_with_speed((100 - x) / 100.0)
            left_motor.go_with_speed((100 - x) / 100.0)
            sleep(0.1)
        right_motor.toggle_direction()
        left_motor.toggle_direction()
