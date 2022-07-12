from pickle import NONE
from urllib import response
from itsdangerous import json
import requests, os, json
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env


data = {"term": "share", "backupterm": None,"defintion": None, "gif": None}

rawData = None

keys = {"WordsAPI": os.getenv("WordsAPI"), "gihpy": os.getenv("gihpy")}


    
# from randon word api
def getJsonRandomWords():
    global data

    url = "https://random-words5.p.rapidapi.com/getRandom"

    headers = {
        "X-RapidAPI-Key": os.getenv("RapidAPIKey"),
        "X-RapidAPI-Host": "random-words5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    response = response.text

    
    data["term"] = response
    

# from words api
def getJsonDefinitions():
    global data

    url = "https://wordsapiv1.p.rapidapi.com/words/" + data["term"] + "/definitions"

    headers = {
        "X-RapidAPI-Key": os.getenv("RapidAPIKey"),
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    response = response.json()
    response = response["definitions"][0]["definition"]

    data["defintion"] = response

# from gihpy api
def getJsonGifpy():
    global data

    url = "https://giphy.p.rapidapi.com/v1/gifs/search"

    querystring = {"q":data["term"],"api_key": os.getenv("gihpy")}

    headers = {
        "X-RapidAPI-Key":   os.getenv("gihpyRapidAPIkey"),
        "X-RapidAPI-Host": "giphy.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    response = response.json()
    response = response["data"][0]["embed_url"]
    print(response)

    data["gif"] = response

def getData():
    getJsonRandomWords()
    getJsonDefinitions()
    getJsonGifpy()

    return data


