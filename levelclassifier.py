from pycorenlp import StanfordCoreNLP


from nltk.parse import CoreNLPParser

nlp = StanfordCoreNLP('http://localhost:9000')
result = CoreNLPParser(url='http://localhost:9000')


def sentiment(sents):

	senti=[]

	for i in sents:

		result = nlp.annotate(i,properties={'timeout':'5000000','annotators': 'sentiment, ner, pos','outputFormat': 'json','timeout': 1000,})

		print("===================================++++++++++++=============================")
		print(result)
		print("===================================++++++++++++=============================")
		for s in result["sentences"]:
			senti.append(s["sentimentValue"])
		
	return senti



