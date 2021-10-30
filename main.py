import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from gpiozero import LED
import board
import busio
import adafruit_vl53l0x
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vl53l0x.VL53L0X(i2c)


# GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
while True:
    print("Range: {0}mm".format(sensor.range))
    time.sleep(1.0)
