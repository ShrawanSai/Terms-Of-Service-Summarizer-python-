	

def highlight(text,phrases,bold,important):
	#print(1111111111111111111)
	s1='<mark style="background-color:pink">'
	s2='<mark>'
	s3='<mark style="background-color:#DCC5E7">'
	end='</mark>'
	#text=''''''
	def insert_dash(string, index,what):
	    return string[:index] + what + string[index:]
	for i in phrases:
	    #print(i)
	    try:
	        
	        start=text.index(i)
	    except:
	        try:
	            x=i.split()
	            x.pop(0)
	            x.pop()
	            x=' '.join(x)
	            start=text.index(i)
	        except:
	            break
	        
	    text=insert_dash(text,start,s2)
	    wordEndIndex = text.index(i) + len(i) 
	    text=insert_dash(text,wordEndIndex,end)

	important=list(set(important))
	bold=list(set(bold))
	for i in bold:
	    #print(i)
	    try:
	        
	        start=text.index(i)
	    except:
	        try:
	            x=i.split()
	            x.pop(0)
	            x.pop()
	            x=' '.join(x)
	            start=text.index(i)
	        except:
	            break
	        
	    text=insert_dash(text,start,s1)
	    wordEndIndex = text.index(i) + len(i) 
	    text=insert_dash(text,wordEndIndex,end)


	for i in important:
	    #print(i)
	    try:
	        
	        start=text.index(i)
	        #print(1)
	    except:
	        try:
	            #print(2)
	            x=i.split()
	            x.pop(0)
	            x.pop()
	            x=' '.join(x)
	            start=text.index(i)
	        except:
	            #print(3)
	            break
	        
	    text=insert_dash(text,start,s3)
	    wordEndIndex = text.index(i) + len(i) 
	    text=insert_dash(text,wordEndIndex,end)
	
	text=f"""{text}"""
	print("""f{text}""")
	return text
