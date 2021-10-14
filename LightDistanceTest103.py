#Source Code: https://kookye.com/2017/06/01/design-sound-light-switch-throught-raspberry-pi-and-sound-light-sensor/
#Source Code: https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/

import RPi.GPIO as GPIO
import time
import os

#initialize pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
photo_ch = 0
buzzer = 14
sound = 17
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

#Initializing
def init():
         GPIO.setwarnings(False)
         GPIO.setmode(GPIO.BCM)
         GPIO.setup(buzzer,GPIO.OUT)
         #GPIO.output(buzzer,GPIO.HIGH)
         GPIO.setup(sound,GPIO.IN,pull_up_down=GPIO.PUD_UP)
         # set up the SPI interface pins
         GPIO.setup(SPIMOSI, GPIO.OUT)
         GPIO.setup(SPIMISO, GPIO.IN)
         GPIO.setup(SPICLK, GPIO.OUT)
         GPIO.setup(SPICS, GPIO.OUT)
         #set GPIO direction (IN / OUT)
         GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
         GPIO.setup(GPIO_ECHO, GPIO.IN)
         pass

#Gives the distance behind
def distance():
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
tooClose = 10
lightDiffThreshold = 15

def main():
         init()
         time.sleep(2)
         i1 = 0
         i2 = 0
         i3 = 0

         del1 = 0
         del2 = 0

       
         while True:
             photo_value = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
             i1 = i2
             i2 = i3
             #equation converts output photo_value to intensity, check what the output is
             i3 = (1024-photo_value)/1024.*100
             
             #see the difference between two flashes, depends on the sampling frequency
             del1 = del2
             del2 = abs(i3-i2)
             dist = distance()
             if (dist <= tooClose) and (del1>lightDiffThreshold) and (del2>lightDiffThreshold):
                 print('EV')
                 time.sleep(1)
             else:
                 print('None')
                 time.sleep(1)



if __name__ =='__main__':
         try:
                  main()
         except KeyboardInterrupt:
                  pass
GPIO.cleanup()
