# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board


# Initialize I2C bus and sensor.
from Motor import Motor

motor_r = Motor(21, 20, 16)
motor_r.go_forward()
motor_l = Motor(13, 19, 26)
motor_l.go_forward()

time.sleep(10)