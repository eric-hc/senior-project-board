import sys
import time

from Adafruit_LED_Backpack import Matrix8x8

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# Run through each pixel individually and turn it on.
# Clear the display buffer.
display.clear()
# Set pixel at position i, j to on.  To turn off a pixel set
# the last parameter to 0.
display.set_pixel(0, 0, 1)
# Write the display buffer to the hardware.  This must be called to
# update the actual display LEDs.
display.write_display()
# Delay for half a second.

for line in sys.stdin:
    print('turn on led')
    display = Matrix8x8.Matrix8x8()
    display.begin()
    display.clear()
    display.set_pixel(0, 0, 1)
    display.write_display()
