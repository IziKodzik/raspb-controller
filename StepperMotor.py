from time import sleep

from gpiozero import LED


class StepperMotor:

    def __init__(self, step_pin_no, dir_pin_no):
        self.step_pin = LED(step_pin_no)
        self.dir_pin = LED(dir_pin_no)

    def take_step(self):
        self.step_pin.off()
        sleep(0.0001)
        self.step_pin.on()
        sleep(0.0001)

    def take_steps(self, step_count):
        for step_no in range(step_count):
            self.take_step()
