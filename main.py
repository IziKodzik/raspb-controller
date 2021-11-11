import time
import board
import digitalio
import adafruit_lis3dh
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Set to appropriate CS pin!
int1 = digitalio.DigitalInOut(board.D6) # Set to correct pin for interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_SPI(spi, cs, int1=int1)