# fading the LED on user input
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
p = GPIO.PWM(LED_PIN, 50)
p.start(0)
try:
	while True:
		pwm = int(input('Enter % brightness:'))
		if pwm > 100:
			exit(0)
		p.ChangeDutyCycle(pwm)
		time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
	exit(0)
