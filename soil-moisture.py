					# VCC -> 3.3 V
					# GND -> GND
					# D0  -> GPIO18
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
MOISTURE_PIN = 18
GPIO.setup(MOISTURE_PIN, GPIO.IN)
try:
	while True:
		data = GPIO.input(MOISTURE_PIN)
		if data == 0:
			print('Soil Moisture Present!')
		else:
			print('NO Moisture')
		time.sleep(0.4)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
