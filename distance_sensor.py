import RPi.GPIO as GPIO                    #Import GPIO library
import time
import os#Import time library
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
TRIG = 12                               #Associate pin 23 to TRIG
ECHO = 18                                  #Associate pin 24 to ECHO
pulse_start = 0
pulse_end=0
print ("Distance measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)                  #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                   #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                 #Set TRIG as LOW
  print ("Waitng For Sensor To Settle")
  time.sleep(2)                            #Delay of 2 seconds

  GPIO.output(TRIG, True)                  #Set TRIG as HIGH
  time.sleep(0.00001)                      #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                 #Set TRIG as LOW

  while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
    pulse_start = time.time()              #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

  distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)            #Round to two decimal points

  if distance < 50: #k whether the distance is within range
    print ("Distance:",distance - 0.5,"cm") #Print distance with 0.5 cm calibration
    os.system("fswebcam -S 20 -r 1280x720 --no-banner DATE.jpg")
  else:
    print ("Distance:",distance - 0.5,"cm")  
    print ("Out Of Range" )
    exit()
       #display out of range
