import smbus2 as smbus
bus = smbus.SMBus(1)
read = bus.read_byte_data(0x1d, 1)
print(read)
bus.close()
