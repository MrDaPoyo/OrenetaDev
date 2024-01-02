# doing it here, because then we'll have it for another time if needed
import requests
from readability.readability import Document
import json
import re

'''
df = open("tools/url-list.txt") 
urls = df.read()
'''

urls = "google.com youtube.com"
urlsSplit =  urls.split(" ") # each url is split by whatever character is in here

contentTitles = []
contentPages = []
contentCombined = ""
contentObj = {"intents": []}



for url in urlsSplit:
    response = requests.get('http://' + url) #Http may be better 
    #considering Ucanet is mostly used by Windows 95 computers that ain't using Https
    doc = Document(response.content)
    title = doc.title()
    summary = doc.summary()
    contentTitles.append(title)
    contentPages.append(summary)
    contentCombined += (title + " " + summary + ",\n")
    contentObj["intents"].append({
        "tag": url, 
        "keywords": (title + " " + summary).split(" "), 
        "response": ["http://"+url]
    })

def printresults():
    print(contentTitles)
    print(contentPages)
    print("--------Results--------")
    print(contentCombined)
    formattedcontent = remove_html_tags(str(contentObj))
    print(formattedcontent) # I'm gonna need this converted to JSON text
    # print(json.dump(contentObj))

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*? \n>')
    return re.sub(clean, '', text)

printresults()