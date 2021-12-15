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
    while not event.is_set():
        dec.wait_for_change()
        hi = hi + 1
    print('exit')


i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)


x = []
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
hits = 0
proc = True
t = Thread(target=count_hits, args=(hits, proc, ))
t.start()
event = Event()
motor1.go_forward()
motor2.go_forward()
time.sleep(2)
motor1.stop()
motor2.stop()
time.sleep(0.5)
event.set()
print(hits)
print('here')
for i in range(1600):
    distance = vl53.range
    x.append(distance)
    stepper.take_step()
time.sleep(1)
stepper.change_dir()

for i in range(1600):
    stepper.take_step()
print('============================================')
for mes in x:
    if (mes < 3000):
        print(mes)
    else:
        print()