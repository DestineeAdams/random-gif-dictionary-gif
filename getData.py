import requests, os
from dotenv import load_dotenv




      
def parseWord( rawJson):
    return rawJson[0]['word']
 
def parseDefinition( rawJson):
    return rawJson[0]['definition']
    
def parseGif( word):
    load_dotenv()
    
    url = f"http://api.giphy.com/v1/gifs/search?q={word}&api_key={os.getenv('giphy')}&limit=1&rating=pg-13"
    
    # url = "http://api.giphy.com/v1/gifs/search?q=word&api_key=j6yGhxux8O6jCCzFbmMp3ODk9N2E6gO7&limit=1&rating=pg-13"
    response = requests.get(url)
    response.status_code
    
    print(url)
    
    if response.status_code == 200:
        rawJson = response.json()
        
        # print(rawJson)
        try:
            info = rawJson["data"][0]["embed_url"]
            return info
          
        except:
            print("somthing went wrong ========== parseGif")
            return "https://giphy.com/embed/UoeaPqYrimha6rdTFV"
          
def getContent():     
    r = requests.get("https://random-words-api.vercel.app/word/")
  
    content = {"word":" ", "definition":" ", "gifURL":" "}

    if r.status_code == 200:
    
        print("200, we may proceed")
    
        content["word"] = parseWord(r.json())
        content["definition"] = parseDefinition(r.json())
        content["gifURL"] = parseGif(content["word"])
    
        return content       

    else: #put in back up words
        return  {"word":"404", "definition":"A 404 error is an HTTP status code that means that the page you were trying to reach on a website couldn't be found on their server.", "gifURL":"https://media.giphy.com/media/UoeaPqYrimha6rdTFV/giphy.gif", "gifAlt":"404"}
        

# getContent()
