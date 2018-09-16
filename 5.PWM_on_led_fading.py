import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
x=GPIO.PWM(11,100)
x.ChangeFrequency(100)
x.start(0)
while(1):
        for i in range(0,100):
                x.ChangeDutyCycle(i)
                i=i+5
                time.sleep(.05)
        for j in range(100,0):
                x.ChangeDutyCycle(j)
                j=j-1
                time.sleep(0.05)

x.stop()
GPIO.cleanup()
