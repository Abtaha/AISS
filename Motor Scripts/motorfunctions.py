class motor1:
        def setup(self):
                import RPi.GPIO as GPIO
                import time
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(7, GPIO.OUT)
                GPIO.setup(5, GPIO.OUT)
                GPIO.output(5, GPIO.LOW)

        def  step(self,_):
                import RPi.GPIO as GPIO
                import time
                GPIO.output(7, GPIO.LOW)
                time.sleep(_)
                GPIO.output(7, GPIO.HIGH)
                time.sleep(_)

        def dir(self,_):
                import RPi.GPIO as GPIO
                if _ == 0:
                        GPIO.setup(3, GPIO.OUT)
                        GPIO.output(3, GPIO.HIGH)
                else:
                        GPIO.setup(3, GPIO.OUT)
                        GPIO.output(3, GPIO.LOW)

        def enable(self,_):
                import RPi.GPIO as GPIO
                if _ == 0:
                        GPIO.setup(5, GPIO.OUT)
                        GPIO.output(5, GPIO.HIGH)
                else:
                        GPIO.setup(5, GPIO.OUT)
                        GPIO.output(5, GPIO.LOW)


class motor2:
        def setup(self):
                import RPi.GPIO as GPIO
                import time
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(12, GPIO.OUT)
                GPIO.setup(10, GPIO.OUT)
                GPIO.output(10, GPIO.LOW)

        def  step(self,_):
                import RPi.GPIO as GPIO
                import time
                GPIO.output(12, GPIO.LOW)
                time.sleep(_)
                GPIO.output(12, GPIO.HIGH)
                time.sleep(_)

        def dir(self,_):
                import RPi.GPIO as GPIO
                if _ == 0:
                        GPIO.setup(8, GPIO.OUT)
                        GPIO.output(8, GPIO.HIGH)
                else:
                        GPIO.setup(8, GPIO.OUT)
                        GPIO.output(8, GPIO.LOW)

        def enable(self,_):
                import RPi.GPIO as GPIO
                if _ == 0:
                        GPIO.setup(10, GPIO.OUT)
                        GPIO.output(10, GPIO.HIGH)
                else:
                        GPIO.setup(10, GPIO.OUT)
                        GPIO.output(10, GPIO.LOW)
