import sys, json, smbus, time, math
from Adafruit_LED_Backpack import Matrix8x8

I2C_address = 0x71  # address of mux changed to avoid conflict with led driver
I2C_bus_number = 1
bus = smbus.SMBus(I2C_bus_number)

display = Matrix8x8.Matrix8x8()
# display.begin()
# display.clear()

# LED on MUX channel 2 = 1**2 channel 1  
bus.write_byte(I2C_address,2**1)

def ledmx(x, y, z):
    bus.write_byte(I2C_address,2**1)  # tell MUX to use LED channel 2 = 1**2 channel 1    time.sleep(0.1)
    display.set_pixel(x, y, z)
    display.write_display()

# acts as a switch statement to map alphabet coordinates to board values
def map(x):
    return {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8
    }[x]

for line in sys.stdin:
    coord = line[:-1]
    print coord
    x = map(coord[:1]) - 1
    y = coord[1:]
    print x, y
    
    ledmx(int(y), x, 1)

