import cmd
from adxl345 import ADXL345
from itg3200 import ITG3200
from vcm5883l import VCM5883L

class IMUInterface(cmd.Cmd):
    intro = 'Welcome to the IMU sensor interface. Type help or ? to list commands.\n'
    prompt = '(IMU) '

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
        try:
            if axis == 'all':
                data = getattr(self, sensor).read_axis_data()
                print(f"{sensor.capitalize()} Data: X={data[0]}, Y={data[1]}, Z={data[2]}")
            else:
                method_name = f"read_{axis}_axis"
                if hasattr(getattr(self, sensor), method_name):
                    data = getattr(getattr(self, sensor), method_name)()
                    print(f"{sensor.capitalize()} {axis.upper()} Axis: {data}")
                else:
                    print(f"No such method '{method_name}' for {sensor}")
        except AttributeError:
            print("Invalid command or sensor. Try again.")


    def do_quit(self, arg):
        'Quit the IMU interface.'
        print("Thank you for using the IMU interface.")
        return True

if __name__ == '__main__':
    IMUInterface().cmdloop()
