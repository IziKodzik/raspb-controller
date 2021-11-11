import time

import adafruit_vl53l0x
import board
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
thanks = adafruit_vl53l0x.VL53L0X(i2c)
while True:
    print("%f"%thanks.distance)
    time.sleep(0.1)