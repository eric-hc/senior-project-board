#!/usr/bin/python

# Change channel of TCA9548A
# Example: sudo ./multiplexer_channel.py 0

import smbus
import time
import sys
import math
from Adafruit_MCP230xx import Adafruit_MCP230xx

bus = smbus.SMBus(1)

mdrd = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]   # mbrd is the 8 columns of the battleship board this sets them to 11111111 : open w
DEVICE = [0x21, 0x22, 0x23, 0x24]  # 4 I2c Device address of the MCP23017s (A0-A2)
GPIOn = [0x12, 0x13]
IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2= output
IODIRB = 0x01 # B Pin direction register
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # B Register for inputs
GPPUA = 0x0C  # Register for Pull ups A
GPPUB = 0x0D  # Register for Pull ups B

I2C_address = 0x71
I2C_bus_number = 1
I2C_ch_0 = 0b00000001
I2C_ch_1 = 0b00000010
I2C_ch_2 = 0b00000100
I2C_ch_3 = 0b00001000
I2C_ch_4 = 0b00010000
I2C_ch_5 = 0b00100000
I2C_ch_6 = 0b01000000
I2C_ch_7 = 0b10000000

channel = [I2C_ch_0, I2C_ch_1, I2C_ch_2, I2C_ch_3, I2C_ch_4, I2C_ch_5, I2C_ch_6, I2C_ch_7]

def I2C_setup(i2c_channel_setup):
    bus = smbus.SMBus(I2C_bus_number)
    bus.write_byte(I2C_address,i2c_channel_setup)
    time.sleep(0.1)
    # print "TCA9548A I2C channel status:", bin(bus.read_byte(I2C_address))

coordinates = []

# top to bottom, 4-7 on ultiplexor
for i in range(4, 8):
    print 'looking at channel', channel[i]
    I2C_setup(channel[i])
    mcp = Aafruit_MCP230XX(busnum = 1, address = 0x20, num_gpios = 16)


# I2C_setup(int(sys.argv[1]))
