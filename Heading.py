from vcm5883l import VCM5883L
import time
import math

def calculate_heading(x, y):
    """Calculate heading in degrees from X and Y"""
    heading_rad = math.atan2(y, x)
    heading_deg = math.degrees(heading_rad)
    return heading_deg + 360 if heading_deg < 0 else heading_deg

def stream_magnetometer():
    magnetometer = VCM5883L()
    try:
        while True:
            x, y, z = magnetometer.read_axis_data()
            heading = calculate_heading(x, y)

            print(f"X: {x}, Y: {y}, Z: {z}")
            print(f"Heading: {heading:.2f}°\n")

            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Program stopped by user")

if __name__ == '__main__':
    stream_magnetometer()
