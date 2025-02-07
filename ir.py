import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
IR_PIN = 18
GPIO.setup(IR_PIN, GPIO.IN)
try:
	while True:
		data = GPIO.input(IR_PIN)
		if data == 0:
			print('Obstacle Detected!')
		else:
			print('NO Obstacle')
		time.sleep(0.4)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
