from pickle import NONE
from urllib import response
import requests
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env


data = {"term": None, "defintion": None, "gif": None}

keys = {"WordsAPI": os.getenv("WordsAPI"), "gihpy": os.getenv("gihpy")}




# use this funtion when use as module 
def getData():
    setAPI_KEYS()

    getSetWord()
    # getSetDef()
    getSetGif()

    return data


def setAPI_KEYS():
    f = open("secret.txt","r")
    lines = f.readlines()

    keys["WordsAPI"] = lines[0].replace("\n","")
    keys["gihpy"] = lines[1]

    f.close()


def setData(key, vulue):
    data[key] = vulue
    

    
def clearDatalist(key):
    setData(str(key), None)

# when something goes wrong fall back on this
def setData404(method):
    if(method == 'term'):
        setData("term", "404 error")

    if(method == 'defintion'):
        setData("defintion", "trigger for an error 404 message is when website content has been removed or moved to another URL.")

    if(method == 'gif'):
        setData("gif", "https://giphy.com/embed/kF0ngyP7S1DfmzKqiN")

    
    

def getSetWord():

    clearDatalist("term")
    
    try: 
        url = "https://wordsapiv1.p.rapidapi.com/words/"

        querystring = {"random":"true"}

        headers = {
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
            'x-rapidapi-key': keys["WordsAPI"]
        }

        r = requests.request("GET", url, headers=headers, params=querystring)



        resjson = r.json()["word"]
        setData("term", resjson)
        
        resjson = r.json()["results"][0]["definition"]
        setData("defintion", resjson)

    except IndexError: 
        print('IndexError, getSetGif')
        setData404("term")
        setData404("defintion")
        print(r.status_code, " from word")


    except KeyError: 
        print('IndexError, getSetGif')
        setData404("term")
        setData404("defintion")
        print(r.status_code, " from word")

def getSetDef():

    return NONE

def getSetGif():
    params = {
        "q": data["term"],
        "apiKey":keys['gihpy'],
        "limit":"2"
    }

    try:
        url = 'https://api.giphy.com/v1/gifs/search?api_key=' + str(params["apiKey"]) + '&limit=' + str(params["limit"]) + '&q=' + str(params["q"])
        
        r = requests.get(url)

        print(r.json()["data"][1]["embed_url"])

        resjson = r.json()["data"][0]["embed_url"]
        setData("gif", resjson)


    except IndexError: 
        print('IndexError, getSetGif')
        setData404("gif")
        print(r.status_code, " from gif")

    except KeyError: 
        print('IndexError, getSetGif')
        setData404("gif")
        print(r.status_code, " from gif")
    


    

# getSetWord()
# getSetDef()
# getSetGif()

print(getData())
