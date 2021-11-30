import time

from Motor import Motor

motor1 = Motor(16, 20, 21)
motor2 = Motor(26, 19, 13)

motor1.go_forward()
motor2.go_forward()
time.sleep(3)