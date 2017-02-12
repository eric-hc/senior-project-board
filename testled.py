# script to test LEDs
import time
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x70, busnum=1) # default IC2 address is 0x70

# initialize display
display.begin()
display.clear()

while True:
    # turn each LED on
    for x in range(3):
        for y in range(3):
            # x =int((xled-1)/3)+1   # anodes numbers starts 1
            # y =  (2+xled)%3   # cathodes number start 0

            # clear buffer
            display.clear()

            # set pixel at location to on
            display.set_pixel(x, y, 1) # 1 is on, 0 is off

            # update LEDs
            print "(",x,", ",y,")"
            display.write_display()

            time.sleep(0.5)


display.clear()
