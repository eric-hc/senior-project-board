import sys, json

from Adafruit_LED_Backpack import Matrix8x8

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

for line in sys.stdin:
    print line[:-1]
    display = Matrix8x8.Matrix8x8()
    display.begin()
    display.clear()
    display.set_pixel(0, 0, 1)
    display.write_display()
