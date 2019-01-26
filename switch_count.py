import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO_OUT = 16
count = 0

try:
  while True:
    if(GPIO.input(GPIO_OUT) == 0):
      count = count + 1
      print("Count : " + str(count))
      while(GPIO.input(GPIO_OUT) == 0):
        time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()