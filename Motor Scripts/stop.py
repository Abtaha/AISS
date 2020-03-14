import motorfunctions as b
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

a=b.motor1()
b=b.motor2()

a.enable(0)
b.enable(0)
