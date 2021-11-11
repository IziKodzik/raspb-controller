# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import adafruit_adxl34x
import adafruit_lis3dh
import board
import busio
addres = 'fx10'

bus = smbus.SMBus(0)


import adafruit_vl53l0x

# Initialize I2C bus and sensor.
from Adafruit_PureIO import smbus
from gpiozero import LED, PWMLED

from Motor import Motor
from Robot import Robot
#
i2c = busio.I2C(board.SCL, board.SDA)
# vl53 = adafruit_vl53l0x.VL53L0X(i2c)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c)
while True:
    time.sleep(0.5)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.
# Main loop will read the range and print it every second.
