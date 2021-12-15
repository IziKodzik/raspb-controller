import sys
import time
from Decoder import Decoder
from Motor import Motor
from StepperMotor import StepperMotor
import board
import busio
import adafruit_vl53l0x
import _thread

hits = 0


def count_hits():
    dec = Decoder(23)
    while True:
        print(hits)
        dec.wait_for_change()
        hits = hits + 1


_thread.start_new_thread(count_hits())
motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)

i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

hits = 0

x = []
for i in range(1600):
    distance = vl53.range
    x.append(distance)
    print(distance)
    stepper.take_step()
time.sleep(1)
print('============================================')
for mes in x:
    if (mes < 3000):
        print(mes)
    else:
        print()
stepper.change_dir()

for i in range(1600):
    stepper.take_step()
