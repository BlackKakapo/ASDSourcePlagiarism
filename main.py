from tkinter import *
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import nltk
from googlesearch import search 
from collections import Counter 
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import string
import io


#Global variable
filename = ""
counter = Counter()
mylist = list

#GUI
top = Tk()
top.title('Plagiarism')
top.state('zoomed')
top.configure(bg='lightgray')

lbl = Label(top, text="File directory")
lbl.configure(bg='lightgray')
lbl.place(x = 170, y = 0)

text = Text(top)
text.place(x = 170, y = 50)

#Function for atrib namefile
def openfunc():
	global filename
	Tk().withdraw()
	filename = askopenfilename()
	lbl.configure(text= filename)

#Function for open, remove, tokenize, find most relevant, search
def start():
	#delete from text window
	global text
	text.delete(1.0,END)
	text.update()

	#open the file
	with io.open(filename, 'r', encoding='utf8') as f:
		file_content = f.read()

	#remove symbols from text
	for char in string.punctuation:
		file_content = file_content.replace(char,' ')
	

	#remove numbers from text
	digit_list = "1234567890"
	for char in digit_list:
		file_content = file_content.replace(char, "")

	#tokenize the text
	tokens = nltk.word_tokenize(file_content)

	#remove stop words
	tokens_without_sw = [word for word in tokens if not word in stopwords.words()]

	#find most relevant words
	global counter
	counter = Counter(tokens_without_sw) 
	tokens_most_common_10 = counter.most_common(10)
	tokens_most_common_15 = counter.most_common(15) 
	tokens_most_common_20 = counter.most_common(20) 
	tokens_most_common_25 = counter.most_common(25) 
	tokens_most_common_30 = counter.most_common(30)


	list_tokens_most_common_10 = ""
	for i in tokens_most_common_10:
		list_tokens_most_common_10 +=  i[0] + " "

	list_tokens_most_common_15 = ""
	for i in tokens_most_common_15:
		list_tokens_most_common_15 +=  i[0] + " "

	list_tokens_most_common_20 = ""
	for i in tokens_most_common_20:
		list_tokens_most_common_20 +=  i[0] + " "

	list_tokens_most_common_25 = ""
	for i in tokens_most_common_25:
		list_tokens_most_common_25 +=  i[0] + " "

	list_tokens_most_common_30 = ""
	for i in tokens_most_common_30:
		list_tokens_most_common_30 +=  i[0] + " "

	#print most relevant words
	print (list_tokens_most_common_10)
	print("\n")
	print (list_tokens_most_common_15)
	print("\n")
	print (list_tokens_most_common_20)
	print("\n")
	print (list_tokens_most_common_25)
	print("\n")
	print (list_tokens_most_common_30)

	

	#search the links
	list1 = []
	print("\n")
	for a in search(str(list_tokens_most_common_10), tld="com", num=5, stop=5, pause=1):
		list1.append(a)
		print(a)
	print("\n")

	#search the links
	print("\n")
	for b in search(str(list_tokens_most_common_15), tld="com", num=5, stop=5, pause=1): 
	    list1.append(b)
	    print(b)
	print("\n")  

	#search the links
	print("\n")
	for c in search(str(list_tokens_most_common_20), tld="com", num=5, stop=5, pause=1): 
	    list1.append(c)
	    print(c)
	print("\n")

	#search the links
	print("\n")
	for d in search(str(list_tokens_most_common_25), tld="com", num=5, stop=5, pause=10): 
	    list1.append(d)
	    print(d)
	print("\n")  

	#search the links
	print("\n")
	for e in search(str(list_tokens_most_common_30), tld="com", num=5, stop=5, pause=1): 
	    list1.append(e)
	    print(e)
	print("\n")  

	#print list of links
	for i in list1:
	    print (i)
	print("\n\n") 

	#remove dublication
	global mylist
	counter = Counter(list1) 
	mylist = counter.most_common(5)
	print(mylist)
	# mylist = list(dict.fromkeys(list1))

	#print links in GUI
	o = 0
	for i in mylist:
		o+=1
		print(o)
		if o == 6:
			break
		text.insert(INSERT,str(i[0]) + "\n\n")
		
	
	

B1 = Button(top, text = "Alege un fișier", command = openfunc, height = 5, width = 20, bg = "orange", fg = "black")
B1.place(x = 0, y = 0)

B2 = Button(top, text = "Start", command = start, height = 5, width = 20, bg = "orange", fg = "black")
B2.place(x = 0, y = 100)

top.mainloop()