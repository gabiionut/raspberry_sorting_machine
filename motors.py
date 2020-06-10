import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

pinForward = 23
pinReverse = 24

pinForwardBand = 22

GPIO.setup(pinForward, GPIO.OUT)
GPIO.setup(pinReverse, GPIO.OUT)
GPIO.setup(pinForwardBand, GPIO.OUT)

p = GPIO.PWM(pinForward, 100)
q = GPIO.PWM(pinReverse, 100)
r = GPIO.PWM(pinForwardBand, 100)

def right():
    p.start(0)
    p.ChangeDutyCycle(100)
    sleep(1.3)
    p.stop()
    
def left():
    print('Left')
    q.start(0)
    q.ChangeDutyCycle(100)
    sleep(1.3)
    q.stop()
    
def start():
    r.start(0)
    
def stop():
    #sleep(0.6)
    #.ChangeDutyCycle(0)
    r.stop()
    print('Stop')
    
def clear():
    GPIO.cleanup()
    
