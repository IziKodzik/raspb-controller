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
    distance = vl53.range
    x.append(distance)
    stepper.take_step()
time.sleep(1)
for mes in x:
    if(mes < 3000):
        print(mes)
    else:
        print()
stepper.change_dir()

for i in range(1600):
    stepper.take_step()