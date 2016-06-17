import smbus
import time

ADDRESS = 0x70          # Device address
REG_START_WRITE = 81    # Register address to take a measurement
REG_START_MEASURE = 0   # Register address to read back measurement

bus = smbus.SMBus(1)    # Create bus

# Signal device to take measurement
bus.write_byte(ADDRESS, REG_START_WRITE)

# Wait for measurement to be acquired
time.sleep(0.1)

# Read measurement data from device
data = bus.read_i2c_block_data(ADDRESS, REG_START_MEASURE)

# Remove leading bit from first byte
newData = [data[0] & 0b1111111, data[1]]

# Format and print data
print(str(newData) + " | " + str((newData[0]<<8) + newData[1]))