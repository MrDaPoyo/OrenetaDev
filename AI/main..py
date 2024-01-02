import random 
import json 
import pickle 
import numpy as np 
import nltk 
from keras.models import load_model 
from nltk.stem import WordNetLemmatizer 
from flask import Flask, request, jsonify, render_template
 
# Importing all the libraries we do need ^
# Loading and setting up stuff 

lemmatizer = WordNetLemmatizer() 
intents = json.loads(open("AI/intents.json").read()) 
words = pickle.load(open('AI/words.pkl', 'rb')) 
classes = pickle.load(open('AI/classes.pkl', 'rb')) 
model = load_model('AI/chatbotmodel.h5') 
  
#cleans the sentence by removing connectors such as "like", "am", "are" and 
# keeps keywords like "popular", "great" and "cool"

def clean_up_sentences(sentence): 
    sentence_words = nltk.word_tokenize(sentence) 
    sentence_words = [lemmatizer.lemmatize(word) 
                      for word in sentence_words] 
    return sentence_words 


def bagw(sentence): 
    sentence_words = clean_up_sentences(sentence) 
    bag = [0]*len(words) 
    for w in sentence_words: 
        for i, word in enumerate(words): 
            if word == w: 
                bag[i] = 1
    return np.array(bag) 
  
def predict_class(sentence): 
    bow = bagw(sentence) 
    res = model.predict(np.array([bow]))[0] 
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) 
               if r > ERROR_THRESHOLD] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_list = [] 
    for r in results: 
        return_list.append({'intent': classes[r[0]], 
                            'probability': str(r[1])}) 
        return return_list 
  
def get_response(intents_list, intents_json): 
    tag = intents_list[0]['intent'] 
    list_of_intents = intents_json['intents'] 
    result = "" 
    for i in list_of_intents: 
        if i['tag'] == tag: 
            result = random.choice(i['response']) 
            break
    return result 
  
print("Chatbot is up!")
  
''' TODO: Replace this with the API 
while True: 
    message = input("") 
    ints = predict_class(message) 
    res = get_response(ints, intents) 
    print(res) '''

#setting up the Flask server

app = Flask(__name__)

# If the user goes to /search-avocadoes, the server will use "avocadoes" as input

@app.route("/search-<user_id>")
def query(user_id):
    message = user_id
    ints = predict_class(message) 
    res = get_response(ints, intents) 
    return jsonify(res), 200


# Enable debug mode, change on production
if __name__ == "__main__":
    app.run(debug=True)