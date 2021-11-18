# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board


# Initialize I2C bus and sensor.
from Motor import Motor
from StepperMotor import StepperMotor

motor_r = Motor(21, 20, 16)
motor_r.go_forward()
motor_l = Motor(13, 19, 26)
motor_l.go_forward()

stepper = StepperMotor(17, 27)
for i in range(100000000000):
    stepper.take_step()

time.sleep(10)