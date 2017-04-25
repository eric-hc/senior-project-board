# game ends, turns off all LEDs
import smbus, sys
from Adafruit_LED_Backpack import Matrix8x8

# MUX stuff
I2C_address = 0x71  # address of mux changed to avoid conflict with led driver
I2C_bus_number = 1
bus = smbus.SMBus(I2C_bus_number)
# bus = smbus.SMBus(1) # Rev 2 Pi uses 1
# this program scans 64 inputs on 4 MCP23017 port exapanders and returns changes

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()
# LED on MUX channel 2 = 1**2 channel 1
bus.write_byte(I2C_address,2**1)
display.begin()
display.clear()

for line in sys.stdin:
    display.write_display()
