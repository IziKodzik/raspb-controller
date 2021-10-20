from gpiozero import PWMLED, LED


class Motor:

    def __init__(self, pwm_pin, dir_pin0, dir_pin1):
        self.pwm_pin = PWMLED(pwm_pin)
        self.dir_pin0 = LED(dir_pin0)
        self.dir_pin0.on()
        self.dir_pin1 = LED(dir_pin1)
        self.dir_pin1.off()

    def go_with_speed(self, speed):
        self.pwm_pin.value = speed

    def toggle_direction(self):
        self.dir_pin0.toggle()
        self.dir_pin1.toggle()

    def go_forward(self):
        self.go_with_speed(1)
        self.dir_pin0.on()
        self.dir_pin1.off()

    def go_backward(self):
        self.go_with_speed(1)
        self.dir_pin0.off()
        self.dir_pin1.on()
