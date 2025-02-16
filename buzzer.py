# Blinking the buzzer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
BUZZER_PIN = 18
GPIO.setup(BUZZER_PIN, GPIO.OUT)
try:
	while True:
		GPIO.output(BUZZER_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(BUZZER_PIN, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
