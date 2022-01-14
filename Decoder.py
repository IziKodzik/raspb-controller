import RPi.GPIO as GPIO


class Decoder:
    def __init__(self, out_pin):
        self.out_pin = out_pin
        GPIO.setup(out_pin, GPIO.IN)

    def wait_for_change(self, condition=False):
        first = GPIO.input(self.out_pin)
        print(first)
        while GPIO.input(self.out_pin) == first and condition:
            pass
