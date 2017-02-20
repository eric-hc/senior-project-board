var http = require('http');
var express = require('express');

var app = express();

app.get('/test', function(req, res) {
    res.status(200).send('Successful');
});

app.listen(3000);

