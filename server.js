require('dotenv').config();
const { request } = require('express');
const express = require('express');
const app = express();
const port = 3000;
var fs = require("fs")
const axios = require('axios');





// grab api keys
apiGiphyKey = process.env.GiphyKey;
apiWordnikKey = process.env.WordnikKey;

// fetch wordnick data (word and it's definition)

// get word json
const getwordURL = "https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=1&api_key="+apiWordnikKey;

async function getWord() {
  const response = await axios.get(getwordURL);
  let gotword = response.data;

  
}

// getWord().catch(error => {console.log(error) });
// console.log("the word is " + getword + "\n");



// build definition URl
const defstart = "https://api.wordnik.com/v4/word.json/";
const defend = "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key="+apiWordnikKey;

//get definition json
// const getdefinitionURL = defstart + getword + defend
// let getdefinition = "-";


// console.log(getword + " definition is " + getdefinition + "\n");



// build gihpy URl
    //get gihpy json




// server files
app.use(express.static('public'));


// server at port
app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`);
  });
