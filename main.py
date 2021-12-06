import time

from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
from luma.core.interface.serial import i2c
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import sh1106

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
print(f"{vl53.range} mm")

for i in range(4 * 200):
    stepper.take_step()
stepper.change_dir()
print(f"{vl53.range} mm")
time.sleep(1)
for i in range(4 * 200):
    stepper.take_step()

serial = i2c(port=1, address=0x3C)

device = sh1106(serial)
with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((30, 40), "SUM", fill="white")
time.sleep(5)