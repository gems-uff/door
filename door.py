import sys
import time
try:
    import RPi.GPIO as GPIO
except ImportError:
    print('Not running in a Raspberry Pi device, but will show GPIO calls.')
    from fake_gpio import FakeGPIO
    GPIO = FakeGPIO()

DOOR = 17 # GPIO id (BCM) to control the door
BUTTON = 23 # GPIO id (BCM) to listen to the button
OPEN_INTERVAL = 1 # Time interval sending open signal (in seconds)

def open_door(channel = None):
    GPIO.output(DOOR, GPIO.HIGH)
    time.sleep(OPEN_INTERVAL)
    GPIO.output(DOOR, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DOOR, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=open_door, bouncetime=300)

try:
    while True:
        code = input()
        open_door()

except KeyboardInterrupt:
    pass

finally:
    GPIO.remove_event_detect(BUTTON)
    GPIO.cleanup()