import time

from Motor import Motor
from StepperMotor import StepperMotor

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)
time.sleep(2)

for i in range(0, 200*8):
    stepper.take_step()
time.sleep(1)

motor1.go_forward()
motor2.go_forward()
time.sleep(10)
motor1.go_backward()
motor2.go_backward()
time.sleep(1)
motor1.go_with_speed(0)
motor2.go_with_speed(0)
stepper.change_dir()
for i in range(0, 200*8):
    stepper.take_step()
time.sleep(1)

time.sleep(3)
