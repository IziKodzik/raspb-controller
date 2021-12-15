import sys
import time
from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
from threading import Thread, Event


def count_hits(hi):
    dec = Decoder(23)
    while True:
        dec.wait_for_change()
        hi = hi + 1


hits = 0
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)


motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)


x = []
# while True:
#     stepper.take_step()
for i in range(1600):
    distance = vl53.range
    x.append(distance)
    stepper.take_step()
time.sleep(1)
stepper.change_dir()
for i in range(1600):
    stepper.take_step()
stepper.change_dir()
print('============================================')
for mes in x:
    if (mes < 3000):
        print(mes)
    else:
        print()
x.clear()
print('============================================')
motor1.go_forward()
motor2.go_forward()
time.sleep(1)
motor1.stop()
motor2.stop()
time.sleep(0.5)
print(hits)
for i in range(1600):
    distance = vl53.range
    x.append(distance)
    print(distance)
    stepper.take_step()
time.sleep(1)
for i in range(1600):
    stepper.take_step()
stepper.change_dir()
print('============================================')
for mes in x:
    if (mes < 3000):
        print(mes)
    else:
        print()
stepper.change_dir()

for i in range(1600):
    stepper.take_step()
