import smbus
import time

REG_START_WRITE = 81    # register address to take a measurement
REG_START_MEASURE = 0   # register address to read back measurement
ADDRESS = 0x70

bus = smbus.SMBus(1)

bus.write_byte(ADDRESS, REG_START_WRITE)
time.sleep(0.5)
bus.read_word_data(ADDRESS, REG_START_MEASURE)