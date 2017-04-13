import sys, json, smbus, time, math
bus = smbus.SMBus(1) # Rev 2 Pi uses 1, Rev 1 uses 0
# Scans 64 inputs on 4 MCP23017 port exapanders and returns changes
board_cols = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]   # 8 columns of the battleship board this sets them to 11111111 : open w
DEVICE = [0x21, 0x22, 0x23, 0x24]  # 4 I2c Device address of the MCP23017s (A0-A2)
GPIOn = [0x12, 0x13]
IODIRA = 0x00 # APin direction register for first 8 ie 1 = input or 2= output
IODIRB = 0x01 # B Pin direction register
GPIOA  = 0x12 # Register for inputs
GPIOB  = 0x13 # B Register for inputs
GPPUA = 0x0C  # Register for Pull ups A
GPPUB = 0x0D  # Register for Pull ups B

for i in range(4):
    bus.write_byte_data(DEVICE[i], IODIRA, 0xFF)
    bus.write_byte_data(DEVICE[i], GPPAU, 0xFF)
    bus.write_byte_data(DEVICE[i], IODIRB, 0xFF)
    bus.write_byte_data(DEVICE[i], GPPUB, 0xFF)

while True:
    # 8 registers/cols
    for i in range(4):
        for j in range(2):
            a = bus.read_byte_data(DEVICE[i], GPIOn[j])
            if a != board_cols[i + j]: # is a change
                c = a ^ board_cols[i + j]
                state = "close"
                if a > board_cols[i + j] : state = "open"
                y = math.frexp(c)[1]
                print c, y, state
                board_cols[i + j] = a
                time.sleep(0.1)

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

ships = json.dumps(data)

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
