#!/usr/bin/python

# remember to change the GPIO values below to match your sensors
# GPIO output = the pin that's connected to "Trig" on the sensor
# GPIO input = the pin that's connected to "Echo" on the sensor

def reading(sensor):
    import time
    import RPi.GPIO as GPIO
   
#    print "warnings false" 
    # Disable any warning message such as GPIO pins in use
    GPIO.setwarnings(False)
    
    # use the values of the GPIO pins, and not the actual pin number
    # so if you connect to GPIO 25 which is on pin number 22, the 
    # reference in this code is 25, which is the number of the GPIO 
    # port and not the number of the physical pin
#    print "setmode"
    GPIO.setmode(GPIO.BCM)
    
    if sensor == 0:
        
#	print "sensor 0"
        # point the software to the GPIO pins the sensor is using
        # change these values to the pins you are using
        # GPIO output = the pin that's connected to "Trig" on the sensor
        # GPIO input = the pin that's connected to "Echo" on the sensor
#	print "sen in out"
        GPIO.setup(2,GPIO.OUT)
        GPIO.setup(3,GPIO.IN)
#        GPIO.setup(4,GPIO.OUT)
        GPIO.output(2, GPIO.LOW)
        
        # found that the sensor can crash if there isn't a delay here
        # no idea why. If you have odd crashing issues, increase delay
#        print "sleep"
#	time.sleep(5)
#        print "woke up"

        # sensor manual says a pulse ength of 10Us will trigger the 
        # sensor to transmit 8 cycles of ultrasonic burst at 40kHz and 
        # wait for the reflected ultrasonic burst to be received
        
        # to get a pulse length of 10Us we need to start the pulse, then
        # wait for 10 microseconds, then stop the pulse. This will 
        # result in the pulse length being 10Us.
        
        # start the pulse on the GPIO pin 
        # change this value to the pin you are using
        # GPIO output = the pin that's connected to "Trig" on the sensor
#	print "start pulse"
#        GPIO.output(2, GPIO.HIGH)
        GPIO.output(2, True)
        
        # wait 10 micro seconds (this is 0.00001 seconds) so the pulse
        # length is 10Us as the sensor expects
        time.sleep(0.00001)
        
        # stop the pulse after the time above has passed
        # change this value to the pin you are using
        # GPIO output = the pin that's connected to "Trig" on the sensor
        GPIO.output(2, False)
#	print "pulse stopped"
 
#        print "led deneme"
#        GPIO.output(4, True)
#        time.sleep(1)
#        GPIO.output(4, False)
#        print "led deneme sonu"

        # listen to the input pin. 0 means nothing is happening. Once a
        # signal is received the value will be 1 so the while loop
        # stops and has the last recorded time the signal was 0
        # change this value to the pin you are using
        # GPIO input = the pin that's connected to "Echo" on the sensor
#        print "start listening silence"
	while GPIO.input(3) == 0:
#          print GPIO.input(3)
          signaloff = time.time()
        
#        print signaloff
#        time.sleep(2)
        # listen to the input pin. Once a signal is received, record the
        # time the signal came through
        # change this value to the pin you are using
        # GPIO input = the pin that's connected to "Echo" on the sensor
#        print "start listening echo"
	while GPIO.input(3) == 1:
#	  print GPIO.input(3)
          signalon = time.time()
        
        # work out the difference in the two recorded times above to 
        # calculate the distance of an object in front of the sensor
#        print signalon
#        print "calculate"
	timepassed = signalon - signaloff
        
        # we now have our distance but it's not in a useful unit of
        # measurement. So now we convert this distance into centimetres
        distance = timepassed * 17000
        print str(distance) + " cm."
        time.sleep(1)
        # return the distance of an object in front of the sensor in cm
        return distance
        
        # we're no longer using the GPIO, so tell software we're done
        GPIO.cleanup()

    else:
        print "Incorrect usonic() function varible."

while 1==1:        
  if reading(0) > 75:
    print "BOS"
  else:
    print "DOLU"
