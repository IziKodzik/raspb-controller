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
print(*x, sep='\n')
time.sleep(1)
stepper.change_dir()

for i in range(1600):
    stepper.take_step()

motor1.go_forward()
motor2.go_backward()
time.sleep(0.25)
motor1.stop()
motor2.stop()