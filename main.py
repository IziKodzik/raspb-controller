# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
import subprocess
import time

import adafruit_adxl34x
import adafruit_ssd1306
import adafruit_vl53l0x
import board

from board import SCL, SDA

# Initialize I2C bus and sensor.
from gpiozero import LED

# from Motor import Motor
from StepperMotor import StepperMotor
import busio
from PIL import Image, ImageDraw, ImageFont
WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

# motor_r = Motor(21, 20, 16)
# motor_r.go_forward()
# motor_l = Motor(13, 19, 26)
# motor_l.go_forward()
#
# stepper = StepperMotor(17, 27)
# while True:
#     time.sleep(0.01)
#     stepper.take_step()
# i2c = busio.I2C(board.SCL, board.SDA)
# vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# while True:
#     print("Range: {0}mm".format(vl53.range))
#     time.sleep(1.0)
# i2c = busio.I2C(board.SCL, board.SDA)
# accelerometer = adafruit_adxl34x.ADXL345(i2c)
#
# while True:
#     print("%f %f %f"%accelerometer.acceleration)
#     time.sleep(1)
i2c = busio.I2C(SCL, SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128,64, i2c)
oled.fill(0)
oled.show()
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)
font = ImageFont.load_default()
text = "Hello World!"
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)
oled.image(image)
oled.show()