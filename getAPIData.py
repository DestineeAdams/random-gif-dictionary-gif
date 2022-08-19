from pickle import NONE
import re
from urllib import response
import requests, os, json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

data = {"term": None, "backupterm": None,"defintion": None, "gif": None}


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
    print(response)
    response = response.text
    print(response)
    data["term"] = response
    # print("-------------------------------------------------",data["term"])
    

# from words api
def getJsonDefinitions():
    global data

    url = "https://wordsapiv1.p.rapidapi.com/words/" + data["term"] + "/definitions"

    headers = {
        "X-RapidAPI-Key": os.getenv("RapidAPIKey"),
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(response)
    # print(type(response.status_code))

    if response.status_code == 200:

        response = response.json()
        response = response["definitions"][0]["definition"]

        data["defintion"] = response

    else:
        data["term"] = "Share"
        data["defintion"] = "A part or portion belonging to, distributed to, contributed by, or owed by a person or group."
        data["gif"] = "https://giphy.com/embed/h2i4CqO3IFwBKLc4DC"
    # IndexError: list index out of range

# from gihpy api
def getJsonGifpy():
    global data

    url = "https://giphy.p.rapidapi.com/v1/gifs/search"

    querystring = {"q":data["term"], "api_key": os.getenv("gihpy"), "rating":"pg-13"}

    headers = {
        "X-RapidAPI-Key": os.getenv("RapidAPIKey"),
        "X-RapidAPI-Host": "giphy.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response)
    response = response.json()
    response = response["data"][0]["embed_url"]
   

    data["gif"] = response

def getData():

    getJsonRandomWords()
    getJsonDefinitions()
    getJsonGifpy()
    
    return data


getData()

