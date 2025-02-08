import RPi.GPIO as GPIO   # D0 -> GPIO18
import time
GPIO.setmode(GPIO.BCM)
LDR_PIN = 18
GPIO.setup(LDR_PIN, GPIO.IN)
try:
	while True:
		data = GPIO.input(LDR_PIN)
		if data == 0:
			print('NO Light!')
		else:
			print('Its Light Now!')
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
