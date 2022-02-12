from urllib import response
import requests
import json


data = {"term": None, "defintion": None, "gif": None}

keys = {"wordnik": None, "gihpy": None}


def getAPI_KEYS():
    f = open("secret.txt","r")
    lines = f.readlines()

    keys["wordnik"] = lines[0].replace("\n","")
    keys["gihpy"] = lines[1]

    f.close()
    

def clearDatalist():
    data["term"] = None
    data["defintion"] = None
    data["gif"] = None
    
    keys['wordnik'] = None
    keys['gihpy'] = None
    



def getWord():
    
    r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=2&maxLength=5&api_key=' + keys['wordnik'])
    
    resjson = r.json()
    # print(resjson)
    data["term"] = resjson["word"]

def getDef():
    
    params = {
        "q":data["term"],
        "apiKey":keys['wordnik'],
        "limit":"2"
    }
    
    url = 'https://api.wordnik.com/v4/word.json/' + params["q"] + '/definitions?limit=' + params["limit"] + '&includeRelated=false&useCanonical=false&includeTags=false&api_key=' + params["apiKey"]
   
    
    r = requests.get(url)
    resjson = r.json()
    resjson = resjson[1]
    data["defintion"] = resjson["text"]
    
def getGif():
    params = {
        "q":"funnycat",
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



getAPI_KEYS()
# clearDatalist()

getWord()
getDef()
getGif()

print(data)
print(keys)
