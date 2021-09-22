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
    led = PWMLED(2)
    for j in range(0, 10):
        for i in range(0, 100):
            led.value = i / 100.0
            sleep(0.01)
        led.off()
