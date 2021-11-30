import time

from Motor import Motor

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)

motor1.go_forward()
motor2.go_forward()
time.sleep(3)