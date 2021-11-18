# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board


# Initialize I2C bus and sensor.
from gpiozero import LED

from Motor import Motor
from StepperMotor import StepperMotor

motor_r = Motor(21, 20, 16)
motor_r.go_forward()
motor_l = Motor(13, 19, 26)
motor_l.go_forward()
led = LED(17)

# stepper = StepperMotor(17, 27)
while True:
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.1)