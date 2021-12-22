class Robot:

    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def go_forward(self):
        self.left_motor.go_forward()
        self.right_motor.go_forward()

    def go_backward(self):
        self.left_motor.go_backward()
        self.right_motor.go_backward()

    def turn_left(self):
        self.left_motor.go_backward()
        self.right_motor.go_forward()

    def turn_right(self):
        self.right_motor.go_backward()
        self.left_motor.go_forward()

    def stop(self):
        self.left_motor.go_with_speed(0)
        self.right_motor.go_with_speed(0)
