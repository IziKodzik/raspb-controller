from time import sleep

import smbus2 as smbus
sleep(0.1)
bus = smbus.SMBus(1)
sleep(1)
for i in range(255):
    print(bus.read_byte_data(0x1d, i))
bus.close()
