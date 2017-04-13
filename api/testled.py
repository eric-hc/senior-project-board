import sys, json
from Adafruit_LED_Backpack import Matrix8x8
# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

display = Matrix8x8.Matrix8x8()
    display.begin()
    display.clear()

# acts as a switch statement to map alphabet coordinates to board values
def map(x):
    return {
        'a': 1,
        'b': 2
    }[x]

for line in sys.stdin:
    var coord = line[:-1]
    print coord

    display.set_pixel(1, 0, 1)
    display.write_display()
