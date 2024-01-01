# doing it here, bc then we have it for another time if needed
# great!
import requests
from readability import Document



for url in urls:
    response = requests.get('http://example.com')
    doc = Document(response.content)
    doc.title()
    doc.summary()
