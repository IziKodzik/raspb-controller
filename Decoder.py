import RPi.GPIO as GPIO


class Decoder:
    def __init__(self, out_pin):
        self.out_pin = out_pin
        GPIO.setup(out_pin, GPIO.IN)

    def wait_for_change(self, condition):
        first = GPIO.input(self.out_pin)
        while GPIO.input(self.out_pin) == first and condition:
            print('n')

