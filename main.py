import time

from Motor import Motor
from StepperMotor import StepperMotor

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)
while True:
    stepper.take_step()
# motor1.go_forward()
# motor2.go_forward()
time.sleep(3)
