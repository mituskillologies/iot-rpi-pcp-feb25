import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TOUCH_PIN = 18   		# SIG -> GPIO18
GPIO.setup(TOUCH_PIN, GPIO.IN)
try:
	while True:
		data = GPIO.input(TOUCH_PIN)
		if data == 0:
			print('Touch Detected!')
		else:
			print('NO Touch')
		time.sleep(0.4)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
