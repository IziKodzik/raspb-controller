import select
from time import sleep

from Motor import Motor
from Robot import Robot

if __name__ == '__main__':
    print('controller running')
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    robot = Robot(left_motor, right_motor)
    while True:
        robot.go_forward()
        sleep(1.5)
        robot.go_backward()
        sleep(1.5)
        robot.turn_left()
        sleep(1.5)
        robot.turn_right()
        sleep(1.5)

