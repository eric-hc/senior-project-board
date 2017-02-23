function ship(name, coords, health) {
    this.name = name;
    this.coords = coords;
    this.health = health;
}

var coords = [
    [0, 0],
    [0, 1],
    [0, 2]
];
var myShip = new ship("battleship", coords, 3);
