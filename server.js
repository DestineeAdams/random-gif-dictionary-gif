require('dotenv').config();
const {
  request
} = require('express');
const express = require('express');
const app = express();
const port = 3000;
var fs = require("fs")
const axios = require('axios');


let data = fs.readFileSync("public/values.json");
let apiData = JSON.parse(data);
console.log(apiData);

function addValue(Key, value) {
  let toWrite;

  if (Key == "word") {
    apiData.word = value;
    console.log(apiData);
    toWrite = JSON.stringify(apiData);
    fs.writeFile("public/values.json", toWrite, () => {
      console.log("done")
    });
  } else if (Key == "definition") {
    apiData.definition = value;
    console.log(apiData);
    toWrite = JSON.stringify(apiData);
    fs.writeFile("public/values.json", toWrite, () => {
      console.log("done")
    });

  } else if (Key == "gifLink") {
    apiData.gifLink = value;
    console.log(apiData);
    toWrite = JSON.stringify(apiData);
    fs.writeFile("public/values.json", toWrite, () => {
      console.log("done")
    });
  } else {
    console.log("key didn't match any keys in the existing JSON file");
    console.log("no changes made");
  }

}





// grab api keys
apiGiphyKey = process.env.GiphyKey;
apiWordnikKey = process.env.WordnikKey;


// fetch wordnick data (word and it's definition)

// get word json
const getwordURL = "https://api.wordnik.com/v4/words.json/randomWords?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=-1&limit=1&api_key=" + apiWordnikKey;

async function getWord() {
  const response = await axios.get(getwordURL);
  let write = response.data[0].word;
  addValue("word", write);
}



// build definition URl
const defstart = "https://api.wordnik.com/v4/word.json/";
const defend = "/definitions?limit=1&includeRelated=false&useCanonical=false&includeTags=false&api_key=" + apiWordnikKey;
const getdefinitionURL = defstart + apiData.word + defend
// const getdefinitionURL = defstart + 'term' + defend


async function getDef() {
  const response = await axios.get(getdefinitionURL);

  let write = response.data[0].text;
  addValue("definition", write);
}



// build gihpy URl

const giphystart = "https://api.giphy.com/v1/gifs/search?api_key=" + apiGiphyKey + "&q=";
const giphyend = apiData.word + "&limit=1&offset=0&rating=pg-13&lang=en";
// const getgiphyURL = giphystart + apiData.word + giphyend
const getgiphyURL = giphystart + "add" + giphyend;

//get gihpy json
async function getGif() {
  const response = await axios.get(getgiphyURL);

  let write = response.data[0].images;
 
  console.log("write is ", write);
  // addValue("gifLink", write);
}


// funtion calls
// getWord().catch(error => {console.log(error) });
// getDef().catch(error => {console.log(error) });
getGif().catch(error => {console.log(error) });



// server files
app.use(express.static('public'));


// server at port
app.listen(port, () => {
  console.log(`app listening at http://localhost:${port}`);
});