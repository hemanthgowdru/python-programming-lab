import RPi.GPIO as GPIO
import time

sensor = 10
LED = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,False)
print=("Initialzing PIR Sensor......")
time.sleep(12)
print=("PIR Ready...")
print=(" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(LED,True)
          print=("Motion Detected")
          while GPIO.input(sensor):
              time.sleep(0.01)
      else:
          GPIO.output(LED,False)


except KeyboardInterrupt:
    GPIO.cleanup()
