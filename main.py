import time
import board
import busio
import adafruit_lis3dh

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_lis3dh.LIS3DH_I2C(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)