import RPi.GPIO as GPIO
import time

# Set up the GPIO pin (GPIO17 is used here)
PIR_PIN = 17

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Wait for sensor to initialize
print("Initializing PIR sensor...")
time.sleep(2)

try:
    print("Waiting for motion...")
    
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            time.sleep(1)  # Delay to avoid multiple triggers
        else:
            print("No Motion")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO settings

