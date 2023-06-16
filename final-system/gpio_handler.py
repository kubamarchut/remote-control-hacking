import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

TRANSMIT_PIN = 37
BUTTON_1_PIN = 3
BUTTON_2_PIN = 7

RED_LED = 15
GREEN_LED = 16
BLUE_LED = 33

GPIO.setup(BUTTON_1_PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_2_PIN, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

def led(r, g, b):
    if r == 1:
        GPIO.output(RED_LED, GPIO.HIGH)
    else:
        GPIO.output(RED_LED, GPIO.LOW)
    if g == 1:
        GPIO.output(GREEN_LED, GPIO.HIGH)
    else:
        GPIO.output(GREEN_LED, GPIO.LOW)
    if b == 1:
        GPIO.output(BLUE_LED, GPIO.HIGH)
    else:
        GPIO.output(BLUE_LED, GPIO.LOW)