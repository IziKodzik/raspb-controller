import time

import RPi.GPIO as GPIO


class Decoder:
    def __init__(self, out_pin):
        self.out_pin = out_pin
        self.decoding = False
        GPIO.setup(out_pin, GPIO.IN)

    def wait_for_change(self):
        first = GPIO.input(self.out_pin)
        self.decoding = True
        while GPIO.input(self.out_pin) == first and self.decoding:
            pass
