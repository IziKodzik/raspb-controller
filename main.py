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
            led.on()
        else:
            led.off()
except KeyboardInterrupt:
    GPIO.cleanup()

#
#
# while True:
#     try:
#         GPIO.output(23, 1)
#         time.sleep(0.00001)
#         GPIO.output(23, 0)
#
#         while GPIO.input(24) == 0:
#             pulse_start = time.time()
#
#         while GPIO.input(24) == 1:
#             pulse_end = time.time()
#
#         pulse_duration = pulse_end - pulse_start
#
#         distance = pulse_duration * 17165
#         distance = round(distance, 1)
#         if distance < 30:
#             GPIO.output(14, 1)
#         else:
#             GPIO.output(14, 0)
#     except KeyboardInterrupt:
#         GPIO.cleanup()
#
