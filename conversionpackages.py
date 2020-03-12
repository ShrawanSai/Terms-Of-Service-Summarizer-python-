import pdfkit
config = pdfkit.configuration(wkhtmltopdf='/home/sam/wkhtmltox/bin/wkhtmltopdf')
import os
from fpdf import FPDF 
import fitz
import warnings
import spacy
import pytextrank
from operator import itemgetter
from math import sqrt
import PyPDF2 

path = "input.pdf"

def getImpPhrases():
    text = pdftotext()
    nlp = spacy.load("en_core_web_sm")
    warnings.filterwarnings("ignore")
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)
    doc = nlp(text)
    
    sent_bounds = [ [s.start, s.end, set([])] for s in doc.sents ]

    limit_phrases = 10
    phrase_id = 0
    unit_vector = []
    for p in doc._.phrases:
        # print(phrase_id, p.text, p.rank)
        unit_vector.append(p.rank)
        for chunk in p.chunks:
            # print(" ", chunk.start, chunk.end)
            for sent_start, sent_end, sent_vector in sent_bounds:
                if chunk.start >= sent_start and chunk.start <= sent_end:
                    # print(" ", sent_start, chunk.start, chunk.end, sent_end)
                    sent_vector.add(phrase_id)
                    break
        phrase_id += 1
        if phrase_id == limit_phrases:
            break

    sum_ranks = sum(unit_vector)
    unit_vector = [ rank/sum_ranks for rank in unit_vector ]

    sent_rank = {}
    sent_id = 0

    for sent_start, sent_end, sent_vector in sent_bounds:
        # print(sent_vector)
        sum_sq = 0.0
        for phrase_id in range(len(unit_vector)):
            # print(phrase_id, unit_vector[phrase_id])
            if phrase_id not in sent_vector:
                sum_sq += unit_vector[phrase_id]**2.0
        sent_rank[sent_id] = sqrt(sum_sq)
        sent_id += 1
    # print(sent_rank)
    sorted(sent_rank.items(), key=itemgetter(1)) 
# to get 
    limit_sentences = 8
    sent_text = {}
    sent_id = 0

    for sent in doc.sents:
        sent_text[sent_id] = sent.text
        sent_id += 1

    num_sent = 0
    Sentences = []
    for sent_id, rank in sorted(sent_rank.items(), key=itemgetter(1)):
        Sentences.append(sent_text[sent_id])
        num_sent += 1
        if num_sent == limit_sentences:
            break

    return Sentences

# def takeInput():
# 	if(url):
# 		pdfkit.from_url("https://help.github.com/en/github/site-policy/github-terms-of-service", "input.pdf", configuration=config)
# 	elif(text):
# 		text = input()
# 		text2 = text.encode('latin-1', 'replace').decode('latin-1')
# 		length = len(text2.split('.'))
# 		texty = text2.split(".")
# 		pdf = FPDF()
# 		pdf.add_page()
# 		for i in range(length):
#             pdf.set_font('arial', 'B', 13.0)
#             pdf.cell(ln=1, h=10, align='L', w=200, txt=texty[i], border=0)
# 		pdf.output('input.pdf', 'F')
# 	elif(pdf):
# 		return 1


def Outputpdf():
    doc = fitz.open(r"input.pdf")
    n= doc.pageCount
    for i in range(0,n):
            page = doc[i]
            text = getImpPhrases()
            for i in text:
                text_instances = page.searchFor(i)
                for inst in text_instances:
                    highlight = page.addHighlightAnnot(inst)
    doc.save("output.pdf", garbage=4, deflate=False, clean=True)


# def findPhrase(inputpdf):
# 	return keywords


def pdftotext():
    pdfFileObj = open(r"input.pdf",'rb') 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    n= pdfReader.numPages  
    a="" 
    for i in range(n):
        pageObj = pdfReader.getPage(i)
        a+= pageObj.extractText()
    pdfFileObj.close()
    return a


def urltopdf(url):
	pdfkit.from_url(url, "input.pdf", configuration=config)

def text2pdf(text):
    #text = input()
    text2 = text.encode('latin-1', 'replace').decode('latin-1')
    length = len(text2.split('.'))
    texty = text2.split(".")
    pdf = FPDF()
    pdf.add_page()
    for i in range(length):
        pdf.set_font('arial', 'B', 13.0)
        pdf.cell(ln=1, h=10, align='L', w=200, txt=texty[i], border=0)
    pdf.output('input.pdf', 'F')

