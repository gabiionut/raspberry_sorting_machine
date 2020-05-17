import RPi.GPIO as GPIO

sensor = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)

def objectDetected():
    return GPIO.input(sensor) == 0