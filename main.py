import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
GPIO.setup(24, GPIO.IN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(23, GPIO.OUT)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.output(23, 0)
print('You ready?')
time.sleep(2)
print('Going...')

GPIO.output(23, 1)
time.sleep(0.00001)
GPIO.output(23, 0)

while GPIO.input(24) == 0:
    pulse_start = time.time()

while GPIO.input(24) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17165
distance = round(distance, 1)
print(f'Dis: {distance}')
time.sleep(0.1)
GPIO.cleanup()