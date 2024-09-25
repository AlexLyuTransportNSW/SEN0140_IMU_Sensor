from itg3200 import ITG3200
import time

def stream_gyroscope():
	gyroscope = ITG3200()
	try:
		while True:
			x, y, z = gyroscope.read_axis_data()
			print(f"X: {x}, Y: {y}, Z: {z}")
			time.sleep(0.2)
	except KeyboardInterrupt:
		print("Program stopped by user")

if __name__=='__main__':
	stream_gyroscope()

