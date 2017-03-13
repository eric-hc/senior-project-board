import smbus
import time
import math
# Module for NOX : Noughts and crosses / Tic Tac Toe Game
# this program scans both registers one device, giving 2 x 8 = 16 inputs, only 9 of these are used in the NOX program
bus = smbus.SMBus(1) # Rev 2 Pi uses 1, Rev 1 Pi uses 0
# this program scans both the A and B registers of one MCP23017 port exapander and returns changes
mbrd = [0xFF,0xFF]   # mbrd is the noughts and crosses board  this sets them to 11111111 : open w
chcol =["A","B","C"]  # column labels
i2cadd=0x21 # the I2c Device address of the MCP23017s (A0-A2)
GPIOn = [0x12, 0x13]
IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2 = output
IODIRB = 0x01 # B Pin direction register
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # B Register for inputs
GPPUA= 0x0C  # Register for Pull ups A
GPPUB= 0x0D  # Register for Pull ups B

# Set all A 8 GPA pins as  input. ie set them to 1 oXFF = 11111111
bus.write_byte_data(i2cadd,IODIRA,0xFF)
# Set pull up on GPA pins .ie from default of 0 to 11111111
bus.write_byte_data(i2cadd,GPPUA,0xFF)
# Set all B 8 GPB pins as  input. ie set them to 1 oXFF = 11111111
bus.write_byte_data(i2cadd,IODIRB,0xFF)
# Set pull up on GPB pins .ie from default of 0 to 11111111
bus.write_byte_data(i2cadd,GPPUB,0xFF)

# LED STUFF BEGIN
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x70, busnum=1) # default IC2 address is 0x70

# initialize display
display.begin()
display.clear()

# now look for a change

# Loop until user presses CTRL-C
while True:
  # read the 8 registers

  for l in range(2):  #loops round both registers of MCP23017
    a = bus.read_byte_data(i2cadd,GPIOn[l])
    if a != mbrd[l]: # there has been a change
      c = a ^ mbrd[l]  # bitwise operation copies the bit if it is set in one operand but not both.
      dirx = "Close"
      if a > mbrd[l] : dirx = "Open"  # if the number gets bigger a 0 has changed to a 1
      y = math.frexp(c)[1]  # calculates integer part of log base 2, which is binary bit position
      w=y+l*8
      print "Square", w, " Reed Switch is" , dirx    # chcol[(w+2)%3], (int((w-1)/3))+1
      if w == 8:
            for x in range(0, 4):
                display.set_pixel(x, 0, 1);
                display.set_pixel(x, 1, 1);
                display.set_pixel(x, 2, 1);
                display.set_pixel(x, 3, 1);
      elif w == 9:
        display.set_pixel(1, 0, 1)
      elif w == 10:
        display.set_pixel(1, 1, 1)
      elif w == 11:
        display.set_pixel(1, 2, 1)
      elif w == 12:
        display.set_pixel(2, 0, 1)
      elif w == 13:
        display.set_pixel(2, 1, 1)
      elif w == 14:
        display.set_pixel(2, 2, 1)
      elif w == 15:
        display.set_pixel(3, 0, 1)
      elif w == 16:
        display.set_pixel(3, 1, 1)
      elif w == 1:
        display.set_pixel(3, 2, 1)

      # update LEDs
      display.write_display()

      mbrd[l]=a  # update the current state of the board
      time.sleep(1)
      display.clear()
      display.write_display()
