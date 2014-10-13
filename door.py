import time
try:
    import RPi.GPIO as GPIO
    RASPBERRY_PI = True
except ImportError:
    RASPBERRY_PI = False

DOOR = 17 # GPIO id (BCM) to control the door
BUTTON = 23 # GPIO id (BCM) to listen to the button
OPEN_INTERVAL = 1 # Time interval sending open signal (in seconds)

def open_door(channel = None):
    if RASPBERRY_PI:
        GPIO.output(DOOR, GPIO.HIGH)
    else:
        print('Opening the door...', end='')

    time.sleep(OPEN_INTERVAL)

    if RASPBERRY_PI:
        GPIO.output(DOOR, GPIO.LOW)
    else:
        print(' ok.')

if RASPBERRY_PI:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(DOOR, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=open_door, bouncetime=200)

try:
    code = input()
    open_door()
except KeyboardInterrupt:
    sys.exit()

if RASPBERRY_PI:
    GPIO.cleanup(DOOR)
    GPIO.cleanup(BUTTON)