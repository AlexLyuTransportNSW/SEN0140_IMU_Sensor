import smbus
import time

class ADXL345:
    def __init__(self, address=0x53, bus_num=1):
        self.address = address
        self.bus = smbus.SMBus(bus_num)
        self.initialize_sensor()

    def initialize_sensor(self):
        # Write code to initialize the ADXL345
        # Set to measure mode
        self.write_byte(0x2D, 0x08)  # POWER_CTL register to measure mode
        # Full resolution and +/- 16g
        self.write_byte(0x31, 0x0B)  # DATA_FORMAT register to full res and +/- 16g

    def write_byte(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def read_byte(self, reg):
        return self.bus.read_byte_data(self.address, reg)

    def read_axis_data(self):
        x = self.read_two_bytes(0x32, 0x33)
        y = self.read_two_bytes(0x34, 0x35)
        z = self.read_two_bytes(0x36, 0x37)
        return x, y, z

    def read_two_bytes(self, lsb_reg, msb_reg):
        lsb = self.read_byte(lsb_reg)
        msb = self.read_byte(msb_reg)
        value = (msb << 8) | lsb
        if value >= 32768:
            value -= 65536
        return value

    def __del__(self):
        self.bus.close()
