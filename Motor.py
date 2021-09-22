from gpiozero import PWMLED


class Motor:

    def __init__(self, pwm_pin):
        self.pwm_pin = PWMLED(pwm_pin)
