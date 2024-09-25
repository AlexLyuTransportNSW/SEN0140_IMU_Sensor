import cmd
from adxl345 import ADXL345
from itg3200 import ITG3200
from vcm5883l import VCM5883L

class IMUInterface(cmd.Cmd):
    intro = 'Welcome to the IMU sensor interface. Type help or ? to list commands.\n'
    prompt = '(IMU) '
    file = None

    def __init__(self):
        super().__init__()
        self.accelerometer = ADXL345()
        self.gyroscope = ITG3200()
        self.magnetometer = VCM5883L()

    def do_read(self, arg):
        'Read sensor data: read [sensor] [axis/all]'
        args = arg.split()
        if len(args) != 2:
            print("Invalid number of arguments")
            return

        sensor, axis = args
        if sensor.lower() == "accelerometer":
            if axis.lower() == "all":
                x, y, z = self.accelerometer.read_axis_data()
                print(f"Accelerometer X: {x}, Y: {y}, Z: {z}")
            else:
                print("Invalid axis, use 'all' for accelerometer")
        elif sensor.lower() == "gyroscope":
            if axis.lower() == "all":
                x, y, z = self.gyroscope.read_axis_data()
                print(f"Gyroscope X: {x}, Y: {y}, Z: {z}")
            else:
                print("Invalid axis, use 'all' for gyroscope")
        elif sensor.lower() == "magnetic":
            if axis.lower() == "all":
                x, y, z = self.magnetometer.read_axis_data()
                print(f"Magnetic Field X: {x}, Y: {y}, Z: {z}")
            elif axis.lower() in ['x', 'y', 'z']:
                value = getattr(self.magnetometer, f"read_{axis.lower()}_axis")()
                print(f"Magnetic Field {axis.upper()}: {value}")
            else:
                print("Invalid axis, use 'x', 'y', 'z', or 'all'")
        else:
            print("Invalid sensor type. Use 'accelerometer', 'gyroscope', or 'magnetic'")

    def do_quit(self, arg):
        'Quit the IMU interface.'
        print("Thank you for using the IMU interface.")
        return True

if __name__ == '__main__':
    IMUInterface().cmdloop()
