# from urllib import response
from asyncio import sleep
import requests
import random, time


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
    
def clearDatalist(key):
    setData(str(key), None)
    # setAPI_KEYS()

def getSetWord():

    clearDatalist("term")
    try:
        r = requests.get('https://api.wordnik.com/v4/words.json/randomWord?hasDictionaryDef=true&excludePartOfSpeech=preposition%2C%20abbreviation%2C%20affix%2C%20article%2C%20auxiliary-verb%2C%20conjunction%2C%20definite-article%2C%20family-name%2C%20given-name%2C%20idiom%2C%20imperative%2C%20noun-plural%2C%20noun-posessive%2C%20past-participle%2C%20phrasal-prefix%2C%20proper-noun%2C%20proper-noun-plural%2C%20proper-noun-posessive%2C%20suffix%2C%20verb-intransitive%2C%20verb-transitive&maxCorpusCount=-1&minDictionaryCount=1&maxDictionaryCount=-1&minLength=5&maxLength=11&api_key=' + keys['wordnik'])
        resjson = r.json()
        setData("term", resjson["word"])
        
    except KeyError:
        # print("KeyError, getSetWord")
        setData("term", "404 error")


def getSetDef():
    
    params = {
        "q": data["term"],
        "apiKey":keys['wordnik'],
        "limit":"2"
    }
    
    try:
        url = 'https://api.wordnik.com/v4/word.json/' + params["q"] + '/definitions?limit=' + params["limit"] + '&includeRelated=false&useCanonical=false&includeTags=false&api_key=' + params["apiKey"]
        r = requests.get(url)
        resjson = r.json()
        resjson = resjson[1]
        setData("defintion", resjson['text'])

    except KeyError:
        # print('KeyError, getSetDef')
        setData("defintion", "trigger for an error 404 message is when website content has been removed or moved to another URL.")
    except TypeError:
        # print('TypeError, getSetDef')
        setData("defintion", "trigger for an error 404 message is when website content has been removed or moved to another URL.")
    except IndexError:
        # print('TypeError, getSetDef')
        # print(data)
        setData("defintion", "trigger for an error 404 message is when website content has been removed or moved to another URL.")
    

def getSetGif():
    params = {
        "q": data["term"],
        "apiKey":keys['gihpy'],
        "limit":"1"
    }
    
    
    try:
        url = 'https://api.giphy.com/v1/gifs/search?api_key=' + params["apiKey"] + '&limit=' + params["limit"] + '&q=' + params["q"]
        
        r = requests.get(url)
        resjson = r.json()
        resjson = resjson["data"]
        resjson = resjson[0]
        resjson = resjson["embed_url"]
        setData("gif", resjson)

    except IndexError: 
        # print('IndexError, getSetGif')
        setData("gif", "https://giphy.com/embed/kF0ngyP7S1DfmzKqiN")
        
    

    


'''testing'''
# for i in range(20):
#     amount = random.randrange(4,10)
#     time.sleep(amount)
#     print(getData())
