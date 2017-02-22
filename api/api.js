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
router.use(function(req, res, next) {
    console.log('Request sent to API...');
    next(); 
});

router.get('/', function (req, res) {
    res.json({
        message: 'This is our API'
    });
});

app.post('/hit', function (req, res) {

});

router.route('/ships')
    .get(function(req, res) {
    res.json({
        message: 'These are your ships, motherfucker'
    });
    })
;

router.route('/hit/:xy')
    .post(function(req, res) {

});

app.use('/api', router);
app.listen(port);
console.log('Magic happening on port ' + port);
