import RPi.GPIO as GPIO
import time
import os
import numpy as np
'''
Intialized Pin to values corresponding to the circuit diagram
and assigned the path for output data to be stored.
'''
GPIO_TRIGGER = 23
GPIO_ECHO = 24
photo_ch = 0
channel = 17
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
red_led = 18
file=open('TestFile5',"w")
file.write("Hey New File")
file.write("\n")

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
def init():
        '''
        This function initialized the input and output pins used by the three sensor and output LED. For this assignment
        we are using BCM order of pin so we set the GPIO pins to BCM inside the infinialization function as well.
        '''
         GPIO.setwarnings(False)
         GPIO.setmode(GPIO.BCM)
         #light: set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         #Distance: set GPIO direction (IN / OUT)
         GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
         GPIO.setup(GPIO_ECHO, GPIO.IN)
         #LED
         GPIO.setup(red_led, GPIO.OUT)
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(channel, GPIO.IN)
         pass

#Gives the distance behind
def distance():
    '''
    The sensor used to get values of this function is Ultrasonic HC-SR04. The distance is calculated with the help
of difference between time taken by ultrasonic wave to hit the object and come back. This wave trigger's after every 0.01ms.
When there is a low the timer will start and when it receives a high the timer will stop. 
'''    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

#read ADC
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        ''' 
        This function is used to get the photon value of light instead of binary value of presence of light. The photo values 
        is then used to compute the intensity of light which is futher utilized to detect the presence of flashing lights.
        This reading reported in terms of Bits
        '''
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)  

        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1

        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

#adjust for experimental conditons
tooClose = 50
lightDiffThreshold = 5
tooLoud = 0
sampleFreq = 0.75

def callback(channel):
'''
This function is called when there is a changes in sound sensor. Once our code senses sound it checks for distance 
of the Emergency vehicle and the presence of flashing lights. The presence of flashing light is detected by taking
the difference in intensity of three consecutive sensed light. If the two consecutive difference is more that the 
specified threshold then it implies there is a flashing light. For our prototype this difference is 5. The driver is alerted about the 
presence of Emergency vehicle is only when it within a specifield limit. The distance bound for our prototype is 50 cm. After a counter of 5 
readings if there is no sound detected the program will leave the callback function and will be called only when there is a change in event. 
We are also appending our output into a .txt file inorder to get the statistics related to experiments. These statistics include Type1 error 
and Type2 error. '''
         musicVolume = 10
         i1 = 0
         i2 = 0
         i3 = 0
         del1 = 0
         del2 = 0
         if GPIO.input(channel): 
             init()
             counter = 0
             while counter < 5:
                 counter += 1
                 photo_value = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
                 i1 = i2
                 i2 = i3
                 #equation converts output photo_value to intensity, check what the output is
                 i3 = (1024-photo_value)/1024.*100
                 
                 #see the difference between two flashes, depends on the sampling frequency
                 del1 = del2
                 del2 = abs(i3-i2)

                 #get current distance
                 dist = distance()


                 if (dist <= tooClose) and (del1>lightDiffThreshold) and \
                 (del2>lightDiffThreshold):
                     #turn on LED
                     GPIO.output(red_led, GPIO.HIGH)
                     #Turn down music
                     musicVolume = 1
                     print('EV!     Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2))
                     line='EV!     Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2)
                     file.write(line)
                     file.write('\n')
                     time.sleep(sampleFreq)
                 elif (counter == 1):
                     print('Sound')
                     line='Sound Detected:'
                     file.write(line)
                     file.write('\n')
                     time.sleep(sampleFreq)
                 elif (counter > 1):
                     print('None,   Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2))
                     line='None,   Distance= ' + str(dist) + '  Light= ' + str(del1) + ', ' + str(del2)
                     file.write(line)
                     file.write('\n')
                     #turn off LED
                     GPIO.output(red_led, GPIO.LOW)
                     time.sleep(sampleFreq)
                 
         
               
GPIO.add_event_detect(channel, GPIO.BOTH)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

while True:
        time.sleep(1)