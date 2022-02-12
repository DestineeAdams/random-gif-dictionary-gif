# from urllib import response
import requests
# import json


data = {"term": None, "defintion": None, "gif": None}

keys = {"wordnik": None, "gihpy": None}



# use this funtion when use as module 
def getData():
    setAPI_KEYS()
    getSetWord()
    getSetDef()
    getSetGif()
    return data
    


def setData(key, vulue):
    data[str(key)] = vulue

def setAPI_KEYS():
    f = open("secret.txt","r")
    lines = f.readlines()

    keys["wordnik"] = lines[0].replace("\n","")
    keys["gihpy"] = lines[1]

    f.close()
    
def clearDatalist():
    setData("term", None)
    setData("defintion", None)
    setData("gif", None)
    
    keys['wordnik'] = None
    keys['gihpy'] = None

def getSetWord():
    r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=2&maxLength=5&api_key=' + keys['wordnik'])
    resjson = r.json()
    setData("term", resjson["word"])

def getSetDef():
    
    params = {
        "q": data["term"],
        "apiKey":keys['wordnik'],
        "limit":"2"
    }
    
    url = 'https://api.wordnik.com/v4/word.json/' + params["q"] + '/definitions?limit=' + params["limit"] + '&includeRelated=false&useCanonical=false&includeTags=false&api_key=' + params["apiKey"]
   
    
    r = requests.get(url)
    resjson = r.json()
    resjson = resjson[0]
    
    setData("defintion", resjson['text'])
    
def getSetGif():
    params = {
        "q": data["term"],
        "apiKey":keys['gihpy'],
        "limit":"1"
    }
    
    url = 'https://api.giphy.com/v1/gifs/search?api_key=' + params["apiKey"] + '&limit=' + params["limit"] + '&q=' + params["q"]

    r = requests.get(url)
    resjson = r.json()
    resjson = resjson["data"]
    resjson = resjson[0]
    resjson = resjson["embed_url"]
    data["gif"] = resjson

    setData("gif", resjson)


# clearDatalist()
# setAPI_KEYS()
# print(getData("term"))
# print(getData("defintion"))
# print(getData("gif"))

# print(getData())
