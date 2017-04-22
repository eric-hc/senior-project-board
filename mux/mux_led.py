# Program designed to test an 8 x 8 array of reed switches and gives the chessboard coordinate and # lights LED on appropriate square
# This program sets up 4 MCP23017 port expanders as inputs as defined in DEVICE[] below
# This program uses the MUX TCA9548A with I2C address changed to x71 by  taking A0 to 3v, this avoided a conflict with the HT16K33 which is also x70.
# HT16K33 wired to channel 1 on MUX
# Each MCP23017 is wired to channels 2, 3, 4, 5, on the MUX
# 
# Will print to the monitor when the state of a chess board switch closes eg A1 Open  or E4 Close
#
# Author : Max Dobres
# Date   : 21 April 2017
#
# http://www.chess.fortherapy.co.uk/
#
# Copyright 2017 Max Dobres
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


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
bus.write_byte(I2C_address,2)  
display.begin()
display.clear()
display.write_display()

def ledmx(x,y,z):
    bus.write_byte(I2C_address,2)  # tell MUX to use LED channel 2 = 1**2 channel 1    time.sleep(0.1)
    display.set_pixel(x, y, z)
    display.write_display()


# first we do a one time setup of the MCPs
for i in range(0,4):  # only device 4 available
# first calculate channel code to send to MUX
# MCPs on channels 2, 3, 4, 5, 
  i2c_channel=2**(i+2) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
  bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel
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
  for k in range(0,4):

    
   
    # time.sleep(0.1)  # just in case  


    for l in range(2):  # for each MCP register A and B
      i2c_channel=2**(k+2) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
      bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel

      a = bus.read_byte_data(DEVICE[k],GPIOn[l])
      if a != mbrd[(k*2)+l]: # there has been a change
        c = a ^ mbrd[(k*2)+l]  # bitwise operation copies the bit if it is set in one operand but not both.
        dirx = "Close"
        z=1
        
        if a > mbrd[(k*2)+l] :
          dirx = "open"  # if the number gets bigger a 0 has changed to a 1
          z=0
        y = math.frexp(c)[1]  # calculates integer part of log base 2, which is binary bit position
        x= (k*2)+l
        print y,x, chcol[x], y, dirx, l
        if y== 8: y=0  #strange wiring on led driver
        ledmx(y,x,z)
        mbrd[(k*2)+l]=a  # update the current state of the board
        # time.sleep(0.1)



