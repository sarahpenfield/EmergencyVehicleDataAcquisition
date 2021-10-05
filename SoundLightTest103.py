import RPi.GPIO as GPIO
import time
import os

buzzer = 14
sound = 17
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

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
         pass


#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
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

photo_ch = 0


lightDiffThreshold = 15

def main():
         init()
         time.sleep(2)
         i1 = 0
         i2 = 0
         i3 = 0

         del1 = 0
         del2 = 0

         
         print"will detect emergency vehicle"
         while True:
             photo_value = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
             i1 = i2
             i2 = i3
             i3 = (1024-photo_value)/1024.*100
             del1 = del2
             del2 = abs(i3-i2)
             print(str(GPIO.input(sound)))
             if (GPIO.input(sound) == False) and (del1>lightDiffThreshold) and (del2>lightDiffThreshold):
                 print('Flashes')
                 time.sleep(1)
                 #sound is high and difference in light is high
             else:
                 print('No Flashes')
                 time.sleep(1)



if __name__ =='__main__':
         try:
                  main()
         except KeyboardInterrupt:
                  pass
GPIO.cleanup()
