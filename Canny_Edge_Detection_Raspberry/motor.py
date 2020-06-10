import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinForward = 20
pinReverse = 21

pinForwardBand = 19
pinReverseBand = 26

GPIO.setup(pinForward, GPIO.OUT)
GPIO.setup(pinReverse, GPIO.OUT)
GPIO.setup(pinForwardBand, GPIO.OUT)
GPIO.setup(pinReverseBand, GPIO.OUT)

#p = GPIO.PWM(pinForward, 100)
#q = GPIO.PWM(pinReverse, 100)
#r = GPIO.PWM(pinForwardBand, 100)

def right():
    GPIO.output(pinForward, 1)
    sleep(0.6)
    GPIO.output(pinForward, 0)
    
def left():
    GPIO.output(pinReverse, 1)
    sleep(0.6)
    GPIO.output(pinReverse, 0)

def start():
    GPIO.output(pinForwardBand, 1)

def stop():
    GPIO.output(pinForwardBand, 0)
    GPIO.output(pinReverseBand, 0)
    
def clear():
    GPIO.cleanup()
    

