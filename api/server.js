var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// nodejs-python communication library
var PythonShell = require('python-shell');
var pyshell = new PythonShell('test.py', {
    mode: 'json'
});

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

// game is ready, get ship data from python script and send to server
socket.on('ships', function (data) {
    console.log(data);

    // sends a message to the Python script via stdin
    pyshell.send('get data');

    pyshell.on('message', function (message) {
        // received a message sent from the Python script
        console.log('pyshell msg:' + message);
    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
        if (err) throw err;
        console.log('pyshell finished');
    });

});

// send ships to server
ship = ["This is static data", "a1", "a2", "a3"];
socket.emit('join', {
    ship
});

// led listener
socket.on('led', function (data) {
    console.log('Getting coordinate');
    console.log(data);
});
