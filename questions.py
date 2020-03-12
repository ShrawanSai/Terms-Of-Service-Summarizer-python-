from nltk.tokenize import sent_tokenize,word_tokenize
#import spacy
import pandas as pd
import numpy as np


def question(text,query):
	print(text)
	test = []
	for i in sent_tokenize(text):
	    if len(i)>2:
	        test.append(i)

	n = 4 
	# using list comprehension 
	final = [test[i * n:(i + 1) * n] for i in range((len(test) + n - 1) // n )]  
	tits=[]
	for j in range(len(final)):
	    tits.append(f'Title{j}')
	

	data=[tits,final]
	df3=pd.DataFrame(data=data)
	df3=df3.transpose()
	df3.columns=['title','paragraphs']
	print(df3)
	#st.text('Hold on this will take some time')


	from ast import literal_eval

	from cdqa.utils.filters import filter_paragraphs
	from cdqa.utils.download import download_model, download_bnpp_data
	from cdqa.pipeline.cdqa_sklearn import QAPipeline

	# Download data and models
	#download_bnpp_data(dir='./data/bnpp_newsroom_v1.1/')
	#download_model(model='bert-squad_1.1', dir='./models')

	# Loading data and filtering / preprocessing the documents
	df = pd.read_csv('D:/devjams/Machine-Learning-Web-Apps-master/NLPIffy_NLP_Based_SpaCy_Flask_App&_API/cdQA/data/bnpp_newsroom_v1.1/bnpp_newsroom-v1.1.csv', converters={'paragraphs': literal_eval})
	df = filter_paragraphs(df)
	#st.text('Please Wait. We are looking for the answer to your question')
	# Loading QAPipeline with CPU version of BERT Reader pretrained on SQuAD 1.1
	cdqa_pipeline = QAPipeline(reader='D:/devjams/Machine-Learning-Web-Apps-master/NLPIffy_NLP_Based_SpaCy_Flask_App&_API/bert_qa_vGPU-sklearn.joblib')

	# Fitting the retriever to the list of documents in the dataframe
	cdqa_pipeline.fit_retriever(df3)
	print(query)
	#st.text('Almost done.......')
	#query = 'Intellectual Property Rights'
	try:
		prediction = cdqa_pipeline.predict(query)
	except Exception as e:
		print(e)
	#st.text(prediction[2])
	return prediction[2]