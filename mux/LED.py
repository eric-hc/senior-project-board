import smbus
import time
import math
from Adafruit_LED_Backpack import Matrix8x8

# MUX stuff
I2C_address = 0x71  # address of mux changed to avoid conflict with led driver
I2C_bus_number = 1
bus = smbus.SMBus(I2C_bus_number)
# bus = smbus.SMBus(1) # Rev 2 Pi uses 1
# this program scans 64 inputs on 4 MCP23017 port exapanders and returns changes 
mbrd = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]   # mbrd is the 8 columns of the chess board this sets them to 11111111 : open w
chcol =["A","B","C","D","E","F","G","H",'X','Y']
DEVICE = [0x21,0x22,0x23, 0x24]  # the 4 I2c Device address of the MCP23017s (A0-A2)
GPIOn = [0x12, 0x13]
IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2= output
IODIRB = 0x01 # B Pin direction register
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # B Register for inputs
GPPUA= 0x0C  # Register for Pull ups A
GPPUB= 0x0D  # Register for Pull ups B

# tested 12/4/2017 
# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()
# LED on MUX channel 2 = 1**2 channel 1  
bus.write_byte(I2C_address,2**1)
display.begin()
display.clear()
display.write_display()

def ledmx(x,y,z):
    bus.write_byte(I2C_address,2**1)  # tell MUX to use LED channel 2 = 1**2 channel 1    time.sleep(0.1)
    display.set_pixel(x, y, z)
    display.write_display()
    
for i in range(8):
    for j in range(8):
        print 'led ', i, j
        ledmx(i, j, 1)
        time.sleep(0.1)

#display.clear()
#display.write_display()
