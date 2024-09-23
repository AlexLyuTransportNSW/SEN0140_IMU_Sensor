from vcm5883l import VCM5883L
import time

def main():
    sensor = VCM5883L()
    try:
        while True:
            x, y, z = sensor.read_axis_data()
            print(f"X: {x}, Y: {y}, Z: {z}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped by user.")

if __name__ == "__main__":
    main()
