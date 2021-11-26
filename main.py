import time

from Motor import Motor

motor = Motor(16, 20, 21)
motor.go_forward()
time.sleep(3)