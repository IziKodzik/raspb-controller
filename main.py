import time

from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
x = []
for i in range(1600):
    stepper.take_step()
    x.append(vl53.range)
stepper.change_dir()
print(x)
time.sleep(1)

for i in range(200):
    stepper.take_step()