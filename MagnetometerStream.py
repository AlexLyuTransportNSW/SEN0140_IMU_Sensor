from vcm5883l import VCM5883L
import time

def stream_magnetometer():
	magnetometer = VCM5883L()
	try:
		while True:
			x, y, z = magnetometer.read_axis_data()
			print(f"X: {x}, Y: {y}, Z: {z}")
			time.sleep(0.5)
	except KeyboardInterrupt:
		print("Program stopped by user")

if __name__=='__main__':
	stream_magnetometer()

