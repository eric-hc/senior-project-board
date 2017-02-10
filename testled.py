# script to test LEDs
import time
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x70, busnum=1) # default IC2 address is 0x70

# initialize display
display.begin()
display.clear()

while True:
    # turn each LED on
    for xled in range(1, 10): # anodes start at 1
        x =int((xled-1)/3)+1   # anodes numbers starts 1
        y =  (2+xled)%3   # cathodes number start 0

        # clear buffer
        display.clear()

        # set pixel at location to on
        display.setpixel(x, y, 1) # 1 is on, 0 is off

        # update LEDs
        display.write_display()

        time.sleep(3)


