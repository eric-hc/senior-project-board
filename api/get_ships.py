import sys, json, smbus, time, math

def get():
  ships = []
  I2C_address = 0x71  # address of mux changed to avoid conflict with led driver
  I2C_bus_number = 1
  bus = smbus.SMBus(I2C_bus_number)
  mbrd = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]   # mbrd is the 8 columns of the chess board this sets them to 11111111 : open w
  chcol =["A","B","C","D","E","F","G","H",'X','Y']
  DEVICE = [0x21,0x22,0x23, 0x20]  # the 4 I2c Device address of the MCP23017s
  GPIOn = [0x12, 0x13]
  IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2= output
  IODIRB = 0x01 # B Pin direction register
  GPIOA  = 0x12 # Register for inputs
  GPIOB  = 0x13 # B Register for inputs
  GPPUA= 0x0C  # Register for Pull ups A
  GPPUB= 0x0D  # Register for Pull ups B

  for i in range(0,4):
    i2c_channel=2**(i+2) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
    bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel
    #print 'check', DEVICE[i]
    bus.write_byte_data(DEVICE[i],IODIRA,0xFF)
    bus.write_byte_data(DEVICE[i],GPPUA,0xFF)
    bus.write_byte_data(DEVICE[i],IODIRB,0xFF)
    bus.write_byte_data(DEVICE[i],GPPUB,0xFF)
  for m in range(0,4):
    channel = 2**(m+2)
    bus.write_byte(I2C_address, channel)
    for n in range(2):
      pos = bus.read_byte_data(DEVICE[m], GPIOn[n])
      if pos != mbrd[(m*2)+n]:
        c = pos ^ mbrd[(m*2)+n]
        xy = math.frexp(c)[1]
        coord = chcol[(m*2)+n]
        ships.append(coord)
        print coord
  return ships

# simple JSON echo script
for line in sys.stdin:
  print json.dumps(get())
