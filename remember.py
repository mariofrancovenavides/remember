
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# python 3.10.8

import random
from wordsList import *

def addWords():
	print("Write the English word")
	wordsEnglish=input()
	print("Write the Spanish meaning")
	wordsSpanish=input()
	words[wordsEnglish]=wordsSpanish
	newwords="words="+str(words)
	print((newwords))
	repalceWordsFile=open("wordsList.py",'w+',encoding='utf-8')
	repalceWordsFile.write(newwords)
	repalceWordsFile.close()

#addWords()

def practice():
	englishList = list(words.keys()) 
	random.shuffle(englishList)
	for englishWord in englishList:
		print(words[englishWord])
		in_englishWord=input()
		i = 0
		while in_englishWord != englishWord:
			i += 1
			print("Incorrect ! \n")
			lettersList = list(englishWord)
			if i > len(lettersList):
				i = len(lettersList)
			for j in range (0,i):
				print(lettersList[j])
			print(words[englishWord])
			in_englishWord=input()

#addWords()
practice()