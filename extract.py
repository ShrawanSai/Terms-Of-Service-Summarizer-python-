import predict
from nltk.tokenize import sent_tokenize,word_tokenize
import spacy

nlp = spacy.load("en_core_web_sm")
def phrases(text):
    c=0
    bold=[]
    for i in sent_tokenize(text):
        if predict.inputfo(i)!= 'Not Found':
            w=word_tokenize(predict.inputfo(i))
            if len(w)>1:
                #print(w)
                ind=0
                l=len(w)

                while True:
                    try:

                        doc=nlp(w[ind])
                        for tok in doc:
                            if tok.pos_ in ['AUX','CONJ','CCONJ','DET','INTJ','PART','PRON','PUNCT','SPACE']:
                                w.pop(0)
                        if w[0]=='be':
                            w.pop(0)

                        else:
                            break
                    except:
                        #print(e)
                        break
                    ind+=1
                while True:
                    try:

                        doc=nlp(w[l])
                        for tok in doc:
                            if tok.pos_ in ['AUX','CONJ','CCONJ','DET','INTJ','PART','PRON','PUNCT','SPACE']:
                                w.pop()

                        else:
                            break
                    except:
                        break
                    l-=1
                if len(w)>1:
                    bold.append(' '.join(w))
                    #print(' '.join(w))
    return bold

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

