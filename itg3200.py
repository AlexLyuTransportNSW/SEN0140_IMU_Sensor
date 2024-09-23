import smbus
import time

class ITG3200:
    def __init__(self, address=0x68, bus_num=1):
        self.address = address
        self.bus = smbus.SMBus(bus_num)
        self.initialize_sensor()

    def initialize_sensor(self):
        # Sample Rate Divider
        self.write_byte(0x15, 0x07)  # Set sample rate to 125 Hz
        # DLPF, Full Scale
        self.write_byte(0x16, 0x1E)  # Â±2000 degrees/sec, low pass filter at 1kHz
        # Power Management
        self.write_byte(0x3E, 0x01)  # Use X gyro oscillator

    def write_byte(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def read_byte(self, reg):
        return self.bus.read_byte_data(self.address, reg)

    def read_axis_data(self):
        x = self.read_two_bytes(0x1D, 0x1E)
        y = self.read_two_bytes(0x1F, 0x20)
        z = self.read_two_bytes(0x21, 0x22)
        return x, y, z

    def read_two_bytes(self, lsb_reg, msb_reg):
        lsb = self.read_byte(msb_reg)
        msb = self.read_byte(lsb_reg)
        return (msb << 8) + lsb

    def __del__(self):
        self.bus.close()

    def read_x_axis(self):
        return self.read_two_bytes(0x32, 0x33)

    def read_y_axis(self):
        return self.read_two_bytes(0x34, 0x35)

    def read_z_axis(self):
        return self.read_two_bytes(0x36, 0x37)
