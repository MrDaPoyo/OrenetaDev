# doing it here, because then we'll have it for another time if needed; Trying to re-build intents.json
import requests
from readability.readability import Document
import json
import re
import time

'''
df = open("tools/url-list.txt") 
urls = df.read()
'''

urls = "google.com youtube.com facebook.com"
urlsSplit =  urls.split(" ") # each url is split by whatever character is in here

contentTitles = []
contentPages = []
contentCombined = ""
contentObj = {"intents": []}



for url in urlsSplit:
    start_time = time.time()
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
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(url + " done in " + str(elapsed_time))
    time.sleep(0)

def printresults():
    print(contentTitles)
    print(contentPages)
    print("--------Results--------")
    print(contentCombined)
    formattedcontent = remove_html_tags(contentObj)
    print(formattedcontent) # I'm gonna need this converted to JSON text
    with open('AI/intents.json', 'w', encoding ='utf8') as json_file: 
        json.dump(formattedcontent, json_file, ensure_ascii = False)

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?&%>')
    return re.sub(clean, '', text)

printresults()