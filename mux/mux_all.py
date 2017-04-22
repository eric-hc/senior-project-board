ch0 = 0b00000001
ch1 = 0b00000010
ch2 = 0b00000100
ch3 = 0b00001000
ch4 = 0b00010000
ch5 = 0b00100000
ch6 = 0b01000000
ch7 = 0b10000000

channels = [ch0, ch1, ch2, ch3, ch4, ch5, ch6, ch7]

import smbus
import time
import math

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

# first we do a one time setup of the MCPs
for i in range(0,4):  # for each of the 4 MCPs
  print 'loop numer ', i
# first calculate channel code to send to MUX
# MCPs on channels 2, 3, 4, 5, 
  i2c_channel=2**(i+4) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
  bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel
  print 'channel ', i2c_channel
  # time.sleep(0.2)
  #for each of the 4 devices
  # Set all A 8 GPA pins as  input. ie set them to 1 oXFF = 11111111
  bus.write_byte_data(DEVICE[i],IODIRA,0xFF)
  # Set pull up on GPA pins .ie from default of 0 to 11111111
  bus.write_byte_data(DEVICE[i],GPPUA,0xFF)
  # Set all B 8 GPB pins as  input. ie set them to 1 oXFF = 11111111
  bus.write_byte_data(DEVICE[i],IODIRB,0xFF)
  # Set pull up on GPB pins .ie from default of 0 to 11111111
  bus.write_byte_data(DEVICE[i],GPPUB,0xFF)

# now look for a change
while True:
  # read the 8 registers
  for k in range(0,1):  
    i2c_channel=2**(k+2) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
    bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel
    # time.sleep(0.1)  # just in case  
    for l in range(2):  # for each MCP register A and B
      a = bus.read_byte_data(DEVICE[k],GPIOn[l])
      if a != mbrd[(k*2)+l]: # there has been a change
        c = a ^ mbrd[(k*2)+l]  # bitwise operation copies the bit if it is set in one operand but not both.
        dirx = "Close"
        if a > mbrd[(k*2)+l] : dirx = "open"  # if the number gets bigger a 0 has changed to a 1
        y = math.frexp(c)[1]  # calculates integer part of log base 2, which is binary bit position
        print chcol[(k*2)+l], y, dirx, l
        mbrd[(k*2)+l]=a  # update the current state of the board
        # time.sleep(0.1)



