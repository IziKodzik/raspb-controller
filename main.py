import time

import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
GPIO.setup(15, GPIO.IN)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.OUT)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)

while True:  # Run forever
    GPIO.output(18, 1)
    start = time.time()
    time.sleep(0.00001)
    GPIO.output(18, 0)
    if GPIO.input(15) == GPIO.HIGH:
        print(start - time.time())