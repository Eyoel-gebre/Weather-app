const express = require('express');
const spawn = require('child_process');
const path = require('path');

const app = express(); //creates main app
app.use(express.static(path.join(__dirname, '/public')));
const PORT = 8080;

//calls python script every 5 mins
setInterval(function() {
	var date = new Date();
	child = spawn.spawn('python3', [path.join(__dirname + '/brains.py')]); 
	console.log('[SUCESSFULLY RAN PYTHON SCIRPT]' + date);
}, 300000);


//Handles get requests by sending static html file that was edited by python script
app.get('/', function (req,res) {
	var date = new Date();
	res.sendFile(path.join(__dirname + '/index.html'));
	console.log('[REQUEST][RESPONSE]' + req.hostname + ' ' + date);
});

//listens at port 8080
app.listen(PORT, function () {
	console.log('[SERVER RUNNING] http://localhost:8080');
	var date = new Date();
	child = spawn.spawn('python3', [path.join(__dirname + '/brains.py')]); 
	console.log('[SUCESSFULLY RAN PYTHON SCIRPT]' + date);
});