import spacy
from nltk.tokenize import sent_tokenize,word_tokenize
nlp = spacy.load("en_core_web_sm")


def bold(text):
    
    bold=[]

    for i in sent_tokenize(text):
        
        doc=nlp(i)
      
        if doc.ents:
            for ent in doc.ents:
                #print(ent.text,'  ',ent.label_)
                if ent.label_ in ['PERSON','NORP','FAC','LOC','WORK_OF_ART','LAW','LANGUAGE','ORDINAL']:


                    if len(word_tokenize(ent.text))>1:
                        #print(word_tokenize(ent.text))
                        bold.append(ent.text)
        
    return bold
def important(text):
    important=[]
    for i in sent_tokenize(text):
        doc2=nlp(i)
        if doc2.ents:    
            for ent in doc2.ents:
                if ent.label_ in ['DATE','TIME','PERCENT','GPE','PRODUCT','EVENT','ORG']:
                    #print('yes')
                    if 'the' in word_tokenize(ent.text) and len(word_tokenize(ent.text))<=2:
                        break
                        
                    important.append(ent.text)
                    #/


  
                    #print(ent.text)
                    
    return important



def notable(text):

	l1=important(text)
	l2=bold(text)

	l=l1+l2
	return l