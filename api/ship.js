function ship(name, coords, health, board) {
    this.name = name;
    this.coords = coords;
    this.health = health;
    this.board = board;
}

/* Get coordinate data from Python script */
var coords = [
    "a2", "b2", "c2"
];

var myShip = new ship("battleship", coords, 3, 1);
