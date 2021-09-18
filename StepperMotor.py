from time import sleep

from gpiozero import LED


class StepperMotor:

    def __init__(self, pin_no):
        self.pin = LED(pin_no)

    def take_step(self):
        self.pin.on()
        self.pin.off()

    def take_steps(self, step_count):
        for step_no in range(step_count):
            self.take_step()
            sleep(0.0000000001)
