import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

# GPIO.setwarnings(False)  # Ignore warning for now
# GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
# GPIO.setup(24, GPIO.IN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.setup(23, GPIO.OUT)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.setup(14, GPIO.OUT)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#
# GPIO.output(23, 0)
# print('You ready?')
# time.sleep(2)
# print('Going...')
from gpiozero import DistanceSensor, LED

sensor = DistanceSensor(trigger=23, echo=24)
print('out')

led = LED(14)
while True:
    if sensor.in_range:
        led.on()
    else:
        led.off()


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
