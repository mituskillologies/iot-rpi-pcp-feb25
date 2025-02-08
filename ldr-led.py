# LDR-D0  -> GPIO18
# LDR-VCC -> 3.3V
# LDR-GND -> GND
# LED-Long  -> GPIO17
# LED-Short -> GND

import RPi.GPIO as GPIO   
import time
GPIO.setmode(GPIO.BCM)
LDR_PIN = 18; 			LED_PIN = 17
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
	while True:
		data = GPIO.input(LDR_PIN)
		if data == 1:
			GPIO.output(LED_PIN, GPIO.HIGH)
		else:
			GPIO.output(LED_PIN, GPIO.LOW)
		time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
