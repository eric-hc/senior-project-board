import json

class Ship(object):
    name = ''
    position = 0
    health = 0
    board = 0

    # constructor/initializer
    def __init__(self, name, pos, health, board):
        self.name = name
        self.position = pos
        self.health = health
        self.board = board

    # other methods
    def valid_board(self):
        return 0 <=self.board <= 1

def make_ship(name, pos, health, board):
    ship = Ship(name, pos, health, board)
    return ship

def toJson():
    data = []
    data['key'] = 'value'
    json_data = json.dumps(data)

def test():
    s = Ship('Ship name', 000, 2, 0)
    print s.name
    print "Is valid board: %s" % s.valid_board()

if __name__ == '__main__':
    test()
