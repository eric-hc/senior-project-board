# script to test LEDs
import time
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x70, busnum=1) # default IC2 address is 0x70

# initialize display
display.begin()
display.clear()

# set pixel at location to on
display.set_pixel(2, 0, 1) # 1 is on, 0 is off
print "turn on"

# update LEDs
display.write_display()
time.sleep(3)

