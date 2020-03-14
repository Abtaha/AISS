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

a.enable(1)
b.enable(1)

#time.sleep(20)
while 1:
        inp = str(raw_input("?>"))

        if inp == "8":
                      i=0
                      while i<200:
                                  a.dir(1)
                                  b.dir(1)
                                  i=i+1
                                  a.step(0.005)
                                  b.step(0.005)

        if inp == "2":
                      i=0
                      while i<200:
                                  a.dir(0)
                                  b.dir(0)
                                  i=i+1
                                  a.step(0.005)
                                  b.step(0.005)


        if inp == "4":
                      i=0
                      while i<20:
                                  a.dir(1)
                                  b.dir(0)
                                  i=i+1
                                  a.step(0.005)
                                  b.step(0.005)

        if inp == "6":
                      i=0
                      while i<20:
                                  a.dir(0)
                                  b.dir(1)
                                  i=i+1
                                  a.step(0.005)
                                  b.step(0.005)

