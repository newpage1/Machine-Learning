from bayes import *
import re

def preparedata(context):
    token = re.compile('\\w*')
    wordlist = token.split(context)
    tokenlist = list()
    for word in worlist:
	    if len(word) > 0:
		    tokenlist.append(word)
    return tokenlist

