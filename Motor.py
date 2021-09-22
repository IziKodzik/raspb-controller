from gpiozero import PWMLED


class Motor:

    def __init__(self, pwm_pin):
        self.pwm_pin = PWMLED(pwm_pin)

    def go_with_speed(self, speed):
        self.pwm_pin.value(speed)

