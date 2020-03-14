from levelclassifier import *
from type_predict import *

def predict(sentences):


	sentiments=sentiment(sentences)
	sclass=pipeline(sentences)

	bad={}
	good={}
	print("_________________________________")
	print("_________________________________")
	print("_________________________________")
	print("_________________________________")

	print(len(sentiments))
	print("_________________________________")

	print(len(sclass))
	print("_________________________________")

	print(len(sentences))
	print("_________________________________")

	for i in range(len(sentences)):
		if sentiments[i]=='1':
			bad.update({sentences[i]:sclass[i]})
		elif sentiments[i]=='3':
			good.update({sentences[i]:sclass[i]})
	
	score=len(bad)-len(good)
	
	return [bad,good,score]


