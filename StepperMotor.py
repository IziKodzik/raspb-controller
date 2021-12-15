from time import sleep

from gpiozero import LED


class StepperMotor:

    def __init__(self, step_pin_no, dir_pin_no):
        self.step_pin = LED(step_pin_no)
        self.dir_pin = LED(dir_pin_no)

    def take_step(self):
        self.step_pin.blink(0.000000000000000000001, 0.000000000000000000000001)


    def change_dir(self):
        self.dir_pin.toggle()

    # def take_steps(self, step_count):
    #     for step_no in range(step_count):
    #         self.take_step()

    def take_steps(self, steps_amount, brake_time=None):
        for step_no in range(steps_amount):
            self.take_step()
            if brake_time is not None:
                sleep(brake_time)
