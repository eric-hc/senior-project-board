var http = require('http');
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;
var router = express.Router();

router.get('/', function(req, res) {
    res.json({ message: 'This is our API' });
});


app.get('/test', function(req, res) {
    res.status(200).send('Successful');
});

app.get('/ships', function(req, res) {
    res.status(200).send('Ships');
});

app.post('/hit', function(req, res) {

});

app.use('/api', router);
app.listen(port);

