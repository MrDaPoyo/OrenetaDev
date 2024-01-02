# required modules to make this bizarre creation work properly
import random 
import json 
import pickle 
import numpy as np 
import nltk 
from keras.models import load_model 
from nltk.stem import WordNetLemmatizer 


lemmatizer = WordNetLemmatizer() 
  
# loading the files we made previously 
intents = json.loads(open("intents.json").read()) 
words = pickle.load(open('words.pkl', 'rb')) 
classes = pickle.load(open('classes.pkl', 'rb')) 
model = load_model('chatbotmodel.h5') 


def clean_up_sentences(sentence): 
    sentence_words = nltk.word_tokenize(sentence) 
    sentence_words = [lemmatizer.lemmatize(word)  
                      for word in sentence_words] 
    return sentence_words 


def bagw(sentence): 
    
    # separate out words from the input sentence 
    sentence_words = clean_up_sentences(sentence) 
    bag = [0]*len(words) 
    for w in sentence_words: 
        for i, word in enumerate(words): 
  
            # check whether the word 
            # is present in the input as well 
            if word == w: 
  
                # as the list of words 
                # created earlier. 
                bag[i] = 1
  
    # return a numpy array 
    return np.array(bag) 

