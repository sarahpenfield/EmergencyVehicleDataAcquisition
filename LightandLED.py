import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LIGHT_PIN = 4
red_led = 18

GPIO.setup(red_led, GPIO.OUT)

GPIO.setup(LIGHT_PIN, GPIO.IN)
lOld = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)
while True:
  if GPIO.input(LIGHT_PIN) != lOld:
    if GPIO.input(LIGHT_PIN):
      print ('No EV')
      GPIO.output(red_led, GPIO.LOW)
    else:
      print ('EV! Get out of way!')
      GPIO.output(red_led, GPIO.HIGH)
  lOld = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)