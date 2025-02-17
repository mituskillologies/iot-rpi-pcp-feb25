import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
IR_PIN = 18						# GPIO18 -> IR-OUT
BUZ_PIN = 17				    # GPIO17 -> Buzzer VCC
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(BUZ_PIN, GPIO.OUT)
try:
	while True:
		data = GPIO.input(IR_PIN)   # Read obstacle
		if data == 0:
			print('Obstacle Detected!')
			GPIO.output(BUZ_PIN, GPIO.HIGH)
		else:
			print('NO Obstacle')
			GPIO.output(BUZ_PIN, GPIO.LOW)
		time.sleep(0.4)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)
