from __future__ import  print_function
import streamlit as st
import re
import nltk
#nltk.download('vader_lexicon')
from nltk.tokenize import sent_tokenize,word_tokenize
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io
import pandas as pd
import questionable_clauses
import getImpPhrases
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from gensim.summarization import summarize
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd

import numpy as np
import pyLDAvis
import pyLDAvis.sklearn
#pyLDAvis.enable_notebook()
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS





#intro
st.title("Welcome to comprehensive understanding section")

st.header("Here you can see the Topic Modelling, Wordcloud and the summary of the TOS")
st.subheader("Below is the input text")





#GET TEXT FROM PDF
@st.cache
def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    return data


#EXTRACT IMPORTANT PHRASES
@st.cache
def importants(texts):
	impsents=getImpPhrases.getImpPhrases(texts)
	print('\n\n\n7654566543\n\n\n')
	print(impsents)
	print('\n\n\n7654566543\n\n\n')
	sents=questionable_clauses.predict(impsents)
	return sents



#READ FILE TEXT
f=open('current.txt','r')
n=f.read()

text=pdfparser(n)
f.close()

textc=text
text=text.split()


#TO PRINT PROPERLY
@st.cache
def normalize(text):
	c=""""""
	for i in range(1,len(text)):
		c+=text[i]
		if i%15==0:
			c+='\n'
		else:
			c+=' '
	text=c
	return text

text=normalize(text)

dubby2=text
dubby=dubby2.split()

st.text(dubby2)
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)




#GET IMPORT SETENCES
@st.cache
def fetchsents(text):


	text=sent_tokenize(text)

	sents=questionable_clauses.predict(text)
	return sents




#CLAUSES
rets=importants(textc)
bad=rets[0]
good=rets[1]
score=rets[2]


baddf=pd.DataFrame(bad.items(), columns=['Clause Senetnce', 'Class of Clause'])
st.header('Questionable Clauses')

st.table(baddf)

    

#SUMMARY

st.header('Summary')


def summary():
	gen_sum=summarize(text, split=True)
		#location = st.multiselect("View Summary",("General","Add ratio","Add maximum wordlimit"))
	location = st.radio("View Summary",("General","Add ratio","Add maximum wordlimit"))
	if location=='General':
		gen_sum=normalize(gen_sum)
		st.warning(gen_sum)
	elif location=='Add ratio':
		st.subheader('Add ratio percentage')

		level = st.slider("Select Ratio level",10,100)
		
		summ=summarize(text, ratio=level/100.0)
			#print(summ)
		st.warning(summ)
		
	elif location=='Add maximum wordlimit':
		level = st.slider("Add word limit",10,len(text.split()))
		summ=summarize(text, word_count=level)
		st.warning(summ)

if st.checkbox("Summary"):
	summary()


if score<0:
	printed='Good'+str(score)
else:
	printed='BAD'+str(score)

st.header('Overall:'+printed)

@st.cache
def wordcloud(textc):
	d = path.dirname(__name__)
	text = textc

	alice_mask = np.array(Image.open(path.join(d, "nigeria.png")))
	stopwords = set(STOPWORDS)
	wc = WordCloud(background_color="black", max_words=2000, mask=alice_mask,stopwords=stopwords)
	wc.generate(text)
	wc.to_file(path.join(d, "alice.png"))
	
wordcloud(textc)

st.header("Wordcloud")
if st.checkbox("Display Wordcloud"):
	img = Image.open("alice.png")
	st.image(img,width=900,caption="Word Cloud")



#
vect=CountVectorizer(ngram_range=(1,1),stop_words='english')
dtm=vect.fit_transform(dubby)
df=pd.DataFrame(dtm.toarray(),columns=vect.get_feature_names())
lda=LatentDirichletAllocation(n_components=5)
lda.fit_transform(dtm)
lda_dtf=lda.fit_transform(dtm)
sorting=np.argsort(lda.components_)[:,::-1]
features=np.array(vect.get_feature_names())
import mglearn
#@st.cache
mglearn.tools.print_topics(topics=range(5), feature_names=features,
sorting=sorting, topics_per_chunk=5, n_words=10)
Agreement_Topic=np.argsort(lda_dtf[:,2])[::-1]
Domain_Name_Topic=np.argsort(lda_dtf[:,4])[::-1]
#@st.cache
zit=pyLDAvis.sklearn.prepare(lda,dtm,vect)
st.header("LDA")
if st.checkbox("Display Topic Modelling Graphs"):
	st.text("Showing Widget on next tab")
	pyLDAvis.show(zit)


