from itg3200 import ITG3200
import time

def main():
    gyro = ITG3200()
    try:
        while True:
            x, y, z = gyro.read_axis_data()
            print(f"Gyro X: {x}, Y: {y}, Z: {z}")
            time.sleep(0.1)  # Adjust sleep time as necessary
    except KeyboardInterrupt:
        print("Program stopped by user.")

if __name__ == "__main__":
    main()
