import time

import RPi.GPIO as GPIO


class UltrasonicSensor:

    def __init__(self, echo_pin, trigger_pin):
        self.echo_pin = echo_pin
        self.range = 30.0
        GPIO.setup(echo_pin, GPIO.IN)
        self.trigger_pin = trigger_pin
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.output(trigger_pin, 0)

    def measure(self):
        GPIO.output(self.trigger_pin, 1)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, 0)

        pulse_start = time.time()
        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()

        pulse_end = time.time()
        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        return pulse_duration * 17165

    def wait_for_in_range(self):
        while not self.in_range():
            1

    def in_range(self):
        return self.measure() < self.range
