# doing it here, bc then we have it for another time if needed
import requests
from flask import Flask
from readability import Document
import jsonify
''' df = open("tools/url-list.txt") 

urls = df.read()'''
urls = "wikipedia.com neal.fun dapoyo.neocities.org theoldnet.com 12thman.com"
urlsSplit =  urls.split(" ") # each url is split by whatever character is in here

contentTitles = []
contentPages = []
contentCombined = ""
contentObj = {"intents": []}

for url in urlsSplit:
    response = requests.get('http://', url) #Http may be better 
    #considering Ucanet is mostly used by Windows 95 computers that ain't using Https
    doc = Document(response.content)
    title = doc.title()
    summary = doc.summary
    contentTitles.appeend(title)
    contentPages.append(summary)
    contentCombined += (title + " " + summary + ",\n")
    contentObj.append({
        "tag": url, 
        "keywords": (title + " " + summary).split(" "), 
        "response": ["http://"+url]
    })

def printresults():
    print(contentTitles)
    print(contentPages)
    print("--------Results--------")
    print(contentCombined)
    print(contentObj) # i'm gonna need this converted to JSON text
    #what do you mean with ^?

printresults()