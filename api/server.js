var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// shit for Python
var sys   = require('util'),
    spawn = require('child_process').spawn,
    send_ships  = spawn('python', ['test.py']);

send_ships.stdout.pipe(process.stdout);
send_ships.stderr.pipe(process.stderr);

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;
var router = express.Router();

// middleware to use for all requests
router.use(function (req, res, next) {
    console.log('Request sent to API...');
    next();
});

router.get('/', function (req, res) {
    res.json({
        message: 'This is our API'
    });
});

router.route('/ships')
    .get(function (req, res) {
        res.json({
            message: 'These are your ships'
        });
    });

app.use('/api', router);
app.listen(port);
console.log('Magic happening on port ' + port);

// connect to server
var io = require('socket.io-client')
var socket = io.connect('http://ec2-34-195-93-38.compute-1.amazonaws.com:3002', {
    reconnect: true
});

// connect listener
socket.on('connect', function (socket) {
    console.log('Connected');
});

// game is ready, get ship data
socket.on('getShips', function (data) {
send_ships.stdout.on('data', function(data) {
   console.log(data.toString());
});
});

// send ships to server
ship = ["a1", "a2", "a3"];
socket.emit('join', {
    ship
});

// led listener
socket.on('led', function (data) {
    console.log('Getting coordinate');
    console.log(data);
});
