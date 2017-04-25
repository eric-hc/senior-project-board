import sys, json, smbus, time, math

ships = []

# new stuff goes here
I2C_address = 0x71  # address of mux changed to avoid conflict with led driver
I2C_bus_number = 1
bus = smbus.SMBus(I2C_bus_number)
# bus = smbus.SMBus(1) # Rev 2 Pi uses 1
# this program scans 64 inputs on 4 MCP23017 port exapanders and returns changes
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

for i in range(0,4):  # for each of the 4 MCPs
# first calculate channel code to send to MUX
# MCPs on channels 2, 3, 4, 5,
  i2c_channel=2**(i+2) # calculates binary that gives channel pos, ie channel 0 is 0b00000001 and channel 4 is b0b00010000
  bus.write_byte(I2C_address,i2c_channel)  # tell MUX to use this channel
  print 'check', DEVICE[i]
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

    for m in range(0,4):
    channel = 2**(m+2)
    bus.write_byte(I2C_address, channel)
    for n in range(2): # A & B
        pos = bus.read_byte_data(DEVICE[m], GPIOn[n])
        if pos != mbrd[(m*2)+n]:
            c = pos ^ mbrd[(m*2)+n]
            xy = math.frexp(c)[1]
            print chcol[(m*2)+n], xy
            ships.append(chcol[(m*2)+n], xy)
    print '',


data = [
    {
            "name": "aircraft-carrier",
            "position": ["a1", "b1", "c1", "d1", "e1"],
            "health": 5,
            "board": "1"
		},
        {
            "name": "cruiser",
            "position": ["a5", "b5"],
            "health": 2,
            "board": "1"
        }
]

ships = json.dumps(ships)

# acts as a switch statement to map board values to readable coordinates
def map(pos):
    return {
        '': a1,
        '': a2,
        '': a3,
        '': a4,
        '': a5,
        '': a6,
        '': a7,
        '': a8,

        '': b1,
        '': b2,
        '': b3,
        '': b4,
        '': b5,
        '': b6,
        '': b7,
        '': b8,

        '': c1,
        '': c2,
        '': c3,
        '': c4,
        '': c5,
        '': c6,
        '': c7,
        '': c8,

        '': d1,
        '': d2,
        '': d3,
        '': d4,
        '': d5,
        '': d6,
        '': d7,
        '': d8,

        '': e1,
        '': e2,
        '': e3,
        '': e4,
        '': e5,
        '': e6,
        '': e7,
        '': e8,

        '': f1,
        '': f2,
        '': f3,
        '': f4,
        '': f5,
        '': f6,
        '': f7,
        '': f8,

        '': g1,
        '': g2,
        '': g3,
        '': g4,
        '': g5,
        '': g6,
        '': g7,
        '': g8,

        '': h1,
        '': h2,
        '': h3,
        '': h4,
        '': h5,
        '': h6,
        '': h7,
        '': h8
    }[pos]

# simple JSON echo script
for line in sys.stdin:
    print json.dumps(data)
