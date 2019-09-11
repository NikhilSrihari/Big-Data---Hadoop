from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import WordNetLemmatizer
import re

stop_words = None
outputfileNames_prefix = "../Data/"
inputfileNames_prefix = "../../../part1/Data/Twitter/"
fileNames = ["atlantic_twitterData", "central_twitterData", "southeast_twitterData", "northwest_twitterData", "pacific_twitterData", "southwest_twitterData",
			"nba_twitterData",
			"atlantic_stwitterData", "central_stwitterData", "southeast_stwitterData", "northwest_stwitterData", "pacific_stwitterData", "southwest_stwitterData",
			"nba_stwitterData"]


def validityCheck(inputString):
	if((any(char.isdigit() for char in inputString))==True):
		if (inputString.find("76")>=0):
			return True
		else:
			return False
	else:
		if ((inputString.lower()).find("advertisement")>=0):
			return False
		else:
			return True



def preprocessFile(fileName):
	lemmatizer = WordNetLemmatizer() 
	readFile = open((inputfileNames_prefix+fileName+".txt"), "r+", encoding="utf8") 
	writeFile = open((outputfileNames_prefix+fileName+"P.txt"), "w", encoding="utf8") 
	for readLine in readFile:
		sent = re.sub(r'[^A-Za-z0-9 ]+', '', readLine.lower())
		word_tokens = word_tokenize(sent)
		for w in word_tokens:
			if (w.isdigit()==True):
				continue
			else:
				if (validityCheck(w)==False):
					continue
			if w not in stop_words: 
				writeFile.write(lemmatizer.lemmatize(w)+" ")
		writeFile.write(" \n ")
	writeFile.close()
	readFile.close()


def main():
	global stop_words
	custom_stop_words = set(["i", "the", "he"])
	stop_words = set(stopwords.words('english'))
	stop_words.update(custom_stop_words)
	for fileName in fileNames:
		try:
			preprocessFile(fileName)
		except:
			continue


main()