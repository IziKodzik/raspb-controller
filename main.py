import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from gpiozero import LED

from UltrasonicSensor import UltrasonicSensor

GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
try:
    sensor = UltrasonicSensor(24, 23)
    sensor.wait_for_in_range()
    led = LED(14)
    while True:
        if not sensor.in_range():
            print(time.time())
        else:
            led.off()
except KeyboardInterrupt:
    GPIO.cleanup()