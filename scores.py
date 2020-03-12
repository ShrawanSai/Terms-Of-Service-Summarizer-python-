#!/usr/bin/env python
# coding: utf-8

# In[52]:


import nltk
nltk.download('vader_lexicon')
from nltk.tokenize import sent_tokenize,word_tokenize
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()
nlp = spacy.load("en_core_web_lg")


# In[53]:



f=open('D:/devjams/Machine-Learning-Web-Apps-master/NLPIffy_NLP_Based_SpaCy_Flask_App&_API/text.txt','r')
text=f.read()


# In[54]:


sents=[]
scores=[]
for i in sent_tokenize(text):
    if len(i)<=4:
        continue
    sents.append(i)
    x=sid.polarity_scores(i)
    #print(x['compound'])
    scores.append(x['compound'])
    
    
    
    


# In[44]:


get_ipython().system('cd D:/devjams/Machine-Learning-Web-Apps-master/NLPIffy_NLP_Based_SpaCy_Flask_App&_API')


# In[45]:


data=[sents,scores]
import numpy as np
data=np.asarray(data)
data=data.transpose()


# In[46]:


import pandas as pd


# In[47]:


df=pd.DataFrame(data=data)


# In[48]:


df.columns=['text','score']


# In[49]:


df=df.sort_values(by=['score'])


# In[50]:


print(df)


# In[51]:


df.values.tolist()


# In[ ]:





# In[ ]:




