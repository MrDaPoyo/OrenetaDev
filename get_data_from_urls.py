# doing it here, bc then we have it for another time if needed
import requests
from readability import Document

df = open("tools/url-list.txt") 

urls = df.read()
urlsSplit =  urls.split("\n")

contentTitles = []
contentPages = []

for url in urls:
    response = requests.get('http://'+url) #Http may better 
    #considering Ucanet is mostly used by Windows 95 computers that ain't using Https
    doc = Document(response.content)
    contentTitles.appeend(doc.title())
    contentPages.append(doc.summary())

print(contentTitles)
print(contentPages)