// import express from 'express';
// import path from 'path';
// import fetch from 'node-fetch';

const express = require('express');
const path = require('path');
const fetch = require('node-fetch');

const app = express();

const hostname = "127.0.0.1";
const port = 3000;


console.log("__dirname", __dirname);

// send and html file to server
app.get('/', (req, res) =>
    res.sendFile(path.join(__dirname, './public/index.html'))
);


// fetch api call
// need to hide api key
const wordURL = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=10&api_key=apiKey";

async () => {
    const response = await fetch(wordURL);
    const data = await response.json();

    console.log(data);
}


// port
app.listen(port, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
})