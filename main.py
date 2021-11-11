from time import sleep

import smbus2 as smbus
sleep(0.1)
bus = smbus.SMBus(1)

while True:
    print(bus.read_byte_data(0x1d, 0x10))
    sleep(0.01)
bus.close()
