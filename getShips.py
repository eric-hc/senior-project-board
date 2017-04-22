#!/usr/bin/python

# Change channel of TCA9548A
# Example: sudo ./multiplexer_channel.py 0

import smbus
import time
import sys
import math

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
    # Set all A 8 GPA pins as  input. ie set them to 1 oXFF = 11111111
    bus.write_byte_data(0x21, IODIRA, 0xFF)
    # Set pull up on GPA pins .ie from default of 0 to 11111111
    bus.write_byte_data(0x21, GPPUA, 0xFF)
    # Set all B 8 GPB pins as  input. ie set them to 1 oXFF = 11111111
    bus.write_byte_data(0x21, IODIRB, 0xFF)
    # Set pull up on GPB pins .ie from default of 0 to 11111111
    bus.write_byte_data(0x21, GPPUB, 0xFF)
    for m in range(1): # register
        for n in range(2): # one row on board
            a = bus.read_byte_data(DEVICE[m], GPIOn[n])
            c = a ^ mdrd[m + n]
            y = math.frexp(c)[1]
            mdrd[m + n] = a
            for x in range(8):
                #print mdrd[x],
                print y, 
            print ''
    print ''


# I2C_setup(int(sys.argv[1]))
