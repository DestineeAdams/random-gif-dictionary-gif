require('dotenv').config();
const {
  request
} = require('express');
const express = require('express');
const app = express();
const port = 3001;
var fs = require("fs")
const http = require('http');
const https = require('https');
const got = require('got');
const axios = require('axios');






function getValue() {
  let data = fs.readFileSync("public/values.json");
  let apifile = JSON.parse(data);

  let toReturn;

  setTimeout(function () {
    toReturn = JSON.stringify(apifile.word);
  }, 2000);
  return toReturn;
}



function clearJson() {
  let data = fs.readFileSync("public/values.json");
  let apiData = JSON.parse(data);
  let toWrite;


  apiData.word = '';
  apiData.definition = '';
  apiData.gifLink = '';

  toWrite = JSON.stringify(apiData);

  fs.writeFile("public/values.json", toWrite, () => {
    // console.log("done");
  });


}


// grab api keys
apiGiphyKey = process.env.GiphyKey;
apiWordnikKey = process.env.WordnikKey;


// build URLS
// const getwordURL = "https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=1&api_key=" + apiWordnikKey;
// const getdefinitionURL = "https://api.wordnik.com/v4/word.json/" + apiData.word + "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key=" + apiWordnikKey;
// const giphyURL = "https://api.giphy.com/v1/gifs/search?api_key=" + apiGiphyKey + "&q=" + apiData.word + "&limit=1&offset=0&rating=pg-13&lang=en";




async function getWord() {
  let data = fs.readFileSync("public/values.json");
  let apiData = JSON.parse(data);
  let toWrite;

  try {
    const getwordURL = "https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&includePartOfSpeech=noun%2Cadjective%2Cpronoun%2Cadverb&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=1&api_key=" + apiWordnikKey;
    const response = await axios.get(getwordURL);
    let write = response.data[0].word;

    apiData.word = write;
    toWrite = JSON.stringify(apiData);

    fs.writeFile("public/values.json", toWrite, () => {
      /*console.log("done")*/
    });
  } catch (error) {
    console.error(error);
  }
}

async function getDef() {
  let data = fs.readFileSync("public/values.json");
  let apiData = JSON.parse(data);
  let toWrite;

  try {
    // const getdefinitionURL = "https://api.wordnik.com/v4/word.json/" + 'term' + "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key=" + apiWordnikKey;
    const getdefinitionURL = "https://api.wordnik.com/v4/word.json/" + apiData.word + "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key=" + apiWordnikKey;
    const response = await axios.get(getdefinitionURL);
    let write = response.data[0].text;

    apiData.definition = write;
    toWrite = JSON.stringify(apiData);


    fs.writeFile("public/values.json", toWrite, () => {
      // console.log("done");
    });

  } catch (error) {
    console.error(error);
  }
}

async function getGif() {
  let data = fs.readFileSync("public/values.json");
  let apiData = JSON.parse(data);


  try {
    const giphyURL = "https://api.giphy.com/v1/gifs/search?api_key=" + apiGiphyKey + "&q=" + apiData.word + "&limit=1&offset=0&rating=pg-13&lang=en";
    // const giphyURL = "https://api.giphy.com/v1/gifs/search?api_key=" + apiGiphyKey + "&q=" + "linnean" + "&limit=1&offset=0&rating=pg-13&lang=en";
    const response = await axios.get(giphyURL);
    let write = response.data.data[0].images.original.url;

    apiData.gifLink = write;
    toWrite = JSON.stringify(apiData);

    fs.writeFile("public/values.json", toWrite, () => {
      /*console.log("done")*/
    });

  } catch (error) {
    console.error(error);

    // in case there is no gif with that key word
    let errorgif = "https://media.giphy.com/media/3o85xFXVQNndE6sy9a/giphy.gif";
    apiData.gifLink = errorgif;
    toWrite = JSON.stringify(apiData);

    fs.writeFile("public/values.json", toWrite, () => {
      /*console.log("done")*/
    });
  }
}


// funtion calls

getWord();
setTimeout(() => {
  getDef()
}, 2000);
setTimeout(() => {
  getGif()
}, 3000);


// serve files
app.use(express.static('public'));


// server at port
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});