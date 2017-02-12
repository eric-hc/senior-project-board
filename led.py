import RPi.GPIO as GPIO
import time
import urllib

url = "http://ec2-34-195-93-38.compute-1.amazonaws.com:3001/test"
response = urllib.urlopen(url).read()
print response

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)

button = False
while 1:
    button = GPIO.input(12)
    if button:
    	GPIO.output(4, False)
    else:
	GPIO.output(4, True)

GPIO.cleanup()
