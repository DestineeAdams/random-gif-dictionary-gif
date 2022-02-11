from urllib import response
import requests
import json

data = ["","",""]


def clearDatalist():
    data[0] = None
    data[1] = None
    data[2] = None

def getWord():
    r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=2&maxLength=5&api_key=9ab90adaddb31b0f1e0080fe71a0c4b6262afe4fe3fb8f6ad')
    
    resjson = r.json()
    data[0] = resjson["word"]

def getDef():
    
    params = {
        "q":data[0],
        "apiKey":"9ab90adaddb31b0f1e0080fe71a0c4b6262afe4fe3fb8f6ad",
        "limit":"2"
    }
    
    url = 'https://api.wordnik.com/v4/word.json/jet/definitions?limit=2&includeRelated=false&useCanonical=false&includeTags=false&api_key=YOURAPIKEY'
    
    url = 'https://api.wordnik.com/v4/word.json/' + params["q"] + '/definitions?limit=' + params["limit"] + '&includeRelated=false&useCanonical=false&includeTags=false&api_key=' + params["apiKey"]
    print(url)
    
    r = requests.get(url)
    resjson = r.json()
    resjson = resjson[1]
    data[1] = resjson["text"]
    
def getGif():
    params = {
        "q":"funnycat",
        "apiKey":"eAwrFQNJYjlWWzsTvn8mMX7h2CScyjYS",
        "limit":"1"
    }
    
    url = 'https://api.giphy.com/v1/gifs/search?api_key=' + params["apiKey"] + '&limit=' + params["limit"] + '&q=' + params["q"]

    r = requests.get(url)
    resjson = r.json()
    resjson = resjson["data"]
    resjson = resjson[0]
    resjson = resjson["embed_url"]
    data[2] = resjson

    
clearDatalist()
getWord()
getDef()
getGif()

for i in data:
    print(i)