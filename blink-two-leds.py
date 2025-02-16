# Blinking the LED
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED_PIN1 = 18
LED_PIN2 = 17
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
try:
	while True:
		GPIO.output(LED_PIN1, GPIO.HIGH)
		GPIO.output(LED_PIN2, GPIO.LOW)
		time.sleep(1)
		GPIO.output(LED_PIN1, GPIO.LOW)
		GPIO.output(LED_PIN2, GPIO.HIGH)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
