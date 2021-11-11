from time import sleep

import smbus2 as smbus
sleep(0.1)
bus = smbus.SMBus(1)
sleep(1)
bus.write_byte(0x1d, 0)
bus.close()
