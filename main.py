import time

from Motor import Motor
from StepperMotor import StepperMotor

motor1 = Motor(21, 20, 16)
motor2 = Motor(13, 19, 26)
stepper = StepperMotor(17, 27)
time.sleep(3)
motor1.go_forward()
motor2.go_forward()

# while True:
#     for i in range(0, 200*8):
#         stepper.take_step()
#     time.sleep(1)

# motor1.go_forward()
# motor2.go_forward()
time.sleep(2)
