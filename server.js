require('dotenv').config();
const express = require('express');
const app = express();
const port = 3000;
const fs = require('fs');

 
// server files
app.use(express.static('public'));

// grab api keys
apiGiphyKey = process.env.GiphyKey;
apiWordnikKey = process.env.WordnikKey;

// fetch wordnick data (word and it's definition)

// get word json
let getword = "https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&api_key="+ apiWordnikKey
let word

console.log(word + "\n");

// build definition URl
let defstart = "https://api.wordnik.com/v4/word.json/"
let defend = "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key="+apiWordnikKey

//get definition json
let getdefinition = defstart+word+defend
let def


console.log(getdefinition);



// build gihpy URl
    //get gihpy json


// server at port
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
  });