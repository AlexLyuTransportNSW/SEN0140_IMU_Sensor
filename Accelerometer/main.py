from adxl345 import ADXL345
import time

def main():
    accelerometer = ADXL345()
    try:
        while True:
            x, y, z = accelerometer.read_axis_data()
            print(f"X: {x}, Y: {y}, Z: {z}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Program stopped by user.")

if __name__ == "__main__":
    main()
