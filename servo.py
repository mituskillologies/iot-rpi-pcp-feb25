import RPi.GPIO as GPIO
import time

# Set up GPIO pin
GPIO.setmode(GPIO.BCM)
servo_pin = 17
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM with 50Hz frequency (common for servos)
pwm = GPIO.PWM(servo_pin, 50)

# Start PWM with 0% duty cycle (servo is at 0°)
pwm.start(0)

def set_angle(angle):
    # Convert angle to duty cycle (0° -> 2.5%, 180° -> 12.5%)
    duty = (angle / 18) + 2.5
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

try:
    while True:
        # Sweep from 0 to 180 degrees and back
        for angle in range(0, 181, 10):  # Increase by 10° each time
            set_angle(angle)
            time.sleep(0.5)
        for angle in range(180, -1, -10):  # Decrease by 10° each time
            set_angle(angle)
            time.sleep(0.5)

except KeyboardInterrupt:
    pass

# Clean up
pwm.stop()
GPIO.cleanup()
