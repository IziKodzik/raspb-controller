# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import adafruit_vl53l0x
import board


# Initialize I2C bus and sensor.
from gpiozero import LED

# from Motor import Motor
from StepperMotor import StepperMotor
import busio
# motor_r = Motor(21, 20, 16)
# motor_r.go_forward()
# motor_l = Motor(13, 19, 26)
# motor_l.go_forward()
#
# stepper = StepperMotor(17, 27)
# while True:
#     time.sleep(0.01)
#     stepper.take_step()
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

while True:
    print("Range: {0}mm".format(vl53.range))
    time.sleep(1.0)