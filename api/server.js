var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

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

// add a listener
socket.on('connect', function (socket) {
    console.log('Connected!');

    // disconnect listener
    socket.on('disconnect', function () {
        console.log('Disconnected');
    });
});

socket.on('led', function (data) {
    console.log('Getting coordinate');
    console.log(data);
});
