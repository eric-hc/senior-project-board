var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

var hits = ''
var board_id = 1

// nodejs-python communication library
var PythonShell = require('python-shell');

app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

var port = process.env.PORT || 8081;
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
/*var socket = io.connect('http://ec2-34-195-93-38.compute-1.amazonaws.com:3002', {
    reconnect: true
});*/
var socket = io.connect('http://34.195.93.38:3002', {
    reconnect: true
});


// connect listener
socket.on('connect', function (socket) {
    console.log('Connected');
});

// game is ready, get ship data from python script and send to server
socket.on('ships', function (data) {
    console.log(data);

    var pyshell = new PythonShell('get_ships.py', {
        mode: 'json'
    });

    // sends a message to the Python script via stdin
    pyshell.send('get data');

    pyshell.on('message', function (message) {
        // received a message sent from the Python script
        console.log(message);
        socket.emit('get-ships', message);
    });

    // end the input stream and allow the process to exit
    pyshell.end(function (err) {
        if (err) throw err;
        console.log('pyshell finished');
    });

});

// led listener
socket.on('led', function (data) {
    var pyled = new PythonShell('led_hit.py', {
        mode: 'text'
    });

    if (data.board == board_id) {
        console.log('Hit coordinate ' + data.cell + ' on board ' + data.board);
        if (hits.length < 1)
            hits = data.cell
        else hits += '\n' + data.cell

        // send cell to python
        pyled.send(hits);
    }

    // get message from python
    pyled.on('message', function (message) {
        console.log(message);
    });

    // end the input stream and allow the process to exit
    pyled.end(function (err) {
        if (err) throw err;
        console.log('finished');
    });
});

socket.on('reset', function () {
    console.log('Game ended, turning off LEDs');

    var pygameover = new PythonShell('game_over.py', {
        mode: 'text'
    });
    hits = ''
    pygameover.send('')

    // end the input stream and allow the process to exit
    pygameover.end(function (err) {
        if (err) throw err;
        console.log('finished');
    });
});

// disconnect
socket.on('disconnect', function () {
    io.emit('Board disconnected');
});
