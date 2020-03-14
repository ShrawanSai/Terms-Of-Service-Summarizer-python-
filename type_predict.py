#imports

from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential,load_model

from keras.preprocessing.text import Tokenizer
from keras.models import Sequential,load_model

import pandas as pd
import numpy as np
import re
import os
import pickle

def preprocess_text(sen):
    # Remove punctuations and numbers
    sen=sen.lower()
    sentence = re.sub('[^a-zA-Z]', ' ', sen)
    

    # Single character removal
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('tokenizer', 'rb')      
    tokenizer = pickle.load(dbfile) 
    dbfile.close() 
    return tokenizer

def pipeline(sentences):
    
    tokenizer=loadData()
    X_pred=[]
    for i in sentences:
        X_pred.append(preprocess_text(i))
        
    #print(X_pred)
    X_pred = tokenizer.texts_to_sequences(X_pred)
    #print(X_pred)
    maxlen=100
    X_pred = pad_sequences(X_pred, padding='post', maxlen=maxlen)

    #print(X_pred)
    
    new_model = load_model('class_pred.h5')
    
    class_tags=['<a', '<ch', '<cr', '<j', '<law', '<ltd', '<ter', '<use']
    
    ys=new_model.predict(X_pred)
    output=[]
    #print(ys)
    for ans in ys:
        output.append(class_tags[np.argmax(ans)])
    
    f=['Arbitration','Unilateral change','Content removal','Jurisdiction','Choice of Law','Limitation of liability','Unilateral termination','Contract by using']

    rett={}
    for i in range(len(class_tags)):
    	rett.update({class_tags[i]:f[i]})
    op=[]
    for i in output:
    	op.append(rett[i])
    return op
    