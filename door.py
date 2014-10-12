import RPi.GPIO as GPIO

DOOR = 17 # GPIO id (BCM) to control the door
OPEN_INTERVAL = 1 # Time interval sending open signal (in seconds)

def open_door:
    GPIO.output(DOOR, GPIO.HIGH)
    time.sleep(OPEN_INTERVAL)
    GPIO.output(DOOR, GPIO.LOW)

# Setup GPIO 17 (BCM) for opening the door
GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR, GPIO.OUT, initial=GPIO.LOW)

open_door