# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import time

import board
import busio

import adafruit_vl53l0x

# Initialize I2C bus and sensor.
from gpiozero import LED, PWMLED

from Motor import Motor
from Robot import Robot
#
# i2c = busio.I2C(board.SCL, board.SDA)
# vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.
# Main loop will read the range and print it every second.
# print("Range: {0}mm".format(vl53.range))
# time.sleep(0.5)
motor0 = Motor(21, 20, 16)
# motor1 = Motor(21, 20, 16)
led = LED(26)
led1 = LED(19)
pwm = PWMLED(13)
led1.on()
led.on()
for x in range(255):
    pwm.value = x/255
    time.sleep(0.01)
while True:
    pass
