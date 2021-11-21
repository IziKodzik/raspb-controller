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
disp = adafruit_ssd1306.SSD1306_I2C(128,32, i2c)
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Draw an ellipse.
draw.ellipse((x, top , x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
# Draw a rectangle.
draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=0)
x += shape_width+padding
# Draw a triangle.
draw.polygon([(x, bottom), (x+shape_width/2, top), (x+shape_width, bottom)], outline=255, fill=0)
x += shape_width+padding
# Draw an X.
draw.line((x, bottom, x+shape_width, top), fill=255)
draw.line((x, top, x+shape_width, bottom), fill=255)
x += shape_width+padding

# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
#font = ImageFont.truetype('Minecraftia.ttf', 8)

# Write two lines of text.
draw.text((x, top),    'Hello',  font=font, fill=255)
draw.text((x, top+20), 'World!', font=font, fill=255)

# Display image.
disp.image(image)
disp.display()