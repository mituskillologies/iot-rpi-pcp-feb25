import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TOUCH_PIN = 18   			# SIG -> GPIO18
LED_PIN = 17
GPIO.setup(TOUCH_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
TOUCH_FLAG = False
try:	
	while True:	
		data = GPIO.input(TOUCH_PIN)
		if data == 0:
			TOUCH_FLAG = not TOUCH_FLAG
		if TOUCH_FLAG:
			GPIO.output(LED_PIN, GPIO.HIGH)
		else:
			GPIO.output(LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
