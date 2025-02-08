import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
buzzer_pin = 17
GPIO.setup(buzzer_pin, GPIO.OUT)
# Frequencies for musical notes (in Hz)
NOTES = {
    'C4': 261,  # Middle C
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 493,
    'C5': 523,  # Higher C
}
NOTE_DURATION = 0.4  
# Function to play a note
def play_note(frequency):
    # Generate a PWM signal at the given frequency
    pwm = GPIO.PWM(buzzer_pin, frequency)
    pwm.start(50)  # 50% duty cycle for sound output
    time.sleep(NOTE_DURATION)  # Wait for the note duration
    pwm.stop()  # Stop the PWM

# Function to play a melody
def play_melody():
    # Simple melody (C4, E4, G4, C5, C4)
    melody = [NOTES['C4'], NOTES['E4'], NOTES['G4'], NOTES['C5'], NOTES['C4']]
    
    # Play each note in the melody
    for note in melody:
        play_note(note)
        time.sleep(0.1)  # Short pause between notes

try:
    print("Playing melody...")
    play_melody()

except KeyboardInterrupt:
    print("Program interrupted. Exiting...")

finally:
    GPIO.cleanup()

