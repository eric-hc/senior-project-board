import smbus
import time
import math

bus = smbus.SMBus(1) # Rev 2 Pi uses 1, Rev 1 uses 0
# Scans 64 inputs on 4 MCP23017 port exapanders and returns changes
mbrd = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]   # mbrd is the 8 columns of the battleship board this sets them to 11111111 : open w
DEVICE = [0x21, 0x22, 0x23, 0x24]  # 4 I2c Device address of the MCP23017s (A0-A2)
GPIOn = [0x12, 0x13]
IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2= output
IODIRB = 0x01 # B Pin direction register
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # B Register for inputs
GPPUA = 0x0C  # Register for Pull ups A
GPPUB = 0x0D  # Register for Pull ups B

for i in range(4):
  # for each of the 4 devices
  # Set all A 8 GPA pins as  input. ie set them to 1 oXFF = 11111111
  bus.write_byte_data(DEVICE[i], IODIRA, 0xFF)
  # Set pull up on GPA pins .ie from default of 0 to 11111111
  bus.write_byte_data(DEVICE[i], GPPUA, 0xFF)
  # Set all B 8 GPB pins as  input. ie set them to 1 oXFF = 11111111
  bus.write_byte_data(DEVICE[i], IODIRB, 0xFF)
  # Set pull up on GPB pins .ie from default of 0 to 11111111
  bus.write_byte_data(DEVICE[i], GPPUB, 0xFF)

while True:
  # read the 8 registers
  for k in range(4):
    for l in range(2):
      a = bus.read_byte_data(DEVICE[k], GPIOn[l])
      if a != mdrd[k + l]: # there has been a change
        c = a ^ mdrd[k + l]  # bitwise operation copies the bit if it is set in one operand but not both
        dirx = "Close"
        if a > mdrd[k + l] : dirx = "Open"  # if the number gets bigger a 0 has changed to a 1
        y = math.frexp(c)[1]  # calculates integer part of log base 2, which is binary bit position
        print c, y, dirx
        mdrd[k + l] = a  # update the current state of the board
        time.sleep(0.1)
        
