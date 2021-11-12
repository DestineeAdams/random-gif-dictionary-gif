require('dotenv').config();
const {
  request
} = require('express');
const express = require('express');
const app = express();
const port = 3001;
const http = require('http');
const https = require('https');
const got = require('got');

var handleapis = require('./handleapis');






// funtion calls

handleapis.getWord();
setTimeout(() => {
  handleapis.getDef()
}, 2000);
setTimeout(() => {
  handleapis.getGif()
}, 3000);


// serve files
app.use(express.static('public'));


// server at port
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});