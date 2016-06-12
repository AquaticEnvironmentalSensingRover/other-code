import smbus

# Register addresses.
MCP9808_REG_CONFIG             = 0x01
MCP9808_REG_UPPER_TEMP         = 0x02
MCP9808_REG_LOWER_TEMP         = 0x03
MCP9808_REG_CRIT_TEMP          = 0x04
MCP9808_REG_AMBIENT_TEMP       = 0x05
MCP9808_REG_MANUF_ID           = 0x06
MCP9808_REG_DEVICE_ID          = 0x07


bus = smbus.SMBus(1)

# Read temperature value
t = bus.read_word_data(0x18,MCP9808_REG_AMBIENT_TEMP)
# Convert to Big Endian
t = ((t << 8) & 0xFF00) + (t >> 8)

# Scale and convert to signed value
temp = (t & 0x0FFF) / 16.0
if t & 0x1000:
	temp -= 256.0