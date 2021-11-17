# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board


# Initialize I2C bus and sensor.
from Motor import Motor

motor = Motor(21, 20, 16)
motor.go_forward()
time.sleep(10)