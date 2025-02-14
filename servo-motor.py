import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servo_pin = 12 
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)  # Start with a duty cycle of 0%

def set_angle(angle):
    # Calculate the duty cycle based on the angle
    # 0 degrees corresponds to 2.5% duty cycle (1ms pulse)
    # 180 degrees corresponds to 12.5% duty cycle (2ms pulse)
    duty_cycle = 2.5 + (angle / 18)  
    # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)  
    # Change the duty cycle to rotate the servo
    #time.sleep(1)  # Wait for the servo to reach the position

try:
    print("Rotating the servo motor...")
    while True:
        for angle in range(0, 181, 10):  
            set_angle(angle)
            time.sleep(0.4)

        for angle in range(180, -1, -10):  
            set_angle(angle)
            time.sleep(0.4)

except KeyboardInterrupt:
    print("Program interrupted. Exiting...")

finally:
    pwm.stop()
    GPIO.cleanup()

