import motorfunctions as b
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

a=b.motor1()
b=b.motor2()

a.setup()
b.setup()

a.dir(1)
b.dir(1)

a.enable(0)
b.enable(0)

time.sleep(2)
i=0

while 1:
        #stat = GPIO.input(11)
        #if stat == "HIGH":
       # a.dir(1)
       # b.dir(1)
        a.step(0.005)
        b.step(0.005)
        #else:
        #        a.step(0.005)
        #        b.step(0.005)
        #        a.dir(0)
        #        b.dir(1)
