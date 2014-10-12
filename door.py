import time
try:
    import RPi.GPIO as GPIO
    RASPBERRY_PI = True
except ImportError:
    RASPBERRY_PI = False

DOOR = 17 # GPIO id (BCM) to control the door
OPEN_INTERVAL = 1 # Time interval sending open signal (in seconds)

def open_door():
    if RASPBERRY_PI:
        GPIO.output(DOOR, GPIO.HIGH)
        time.sleep(OPEN_INTERVAL)
        GPIO.output(DOOR, GPIO.LOW)
    else:
        print('Opening the door.')

if RASPBERRY_PI:
    # Setup GPIO 17 (BCM) for opening the door
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(DOOR, GPIO.OUT, initial=GPIO.LOW)

open_door()

if RASPBERRY_PI: GPIO.cleanup(DOOR)