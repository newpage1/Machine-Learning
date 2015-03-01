from numpy import *
def createlist(dataset):
    """
    select the word from the dataset one by one
    """
    vocabset = set([])
    for document in dataset:
	    vocabset = vocabset|set(document)
    return list(vocabset)

def word2vec(vocablist,inputset):
    returnvec = [0]*len(vocablist)
    for word in inputlist:
	    if word in vocablist:
		    returnvec[vocablist.index(word)] = 1
	    else:
		    print "%s is not in the vocabulary" %word
    return returnvec

def train(tmatrix,category)
    numdocs = len(tmatrix)
    numwords = len(tmatrix[0])
    pa = sum(category)/float(numdocs)
    pnum = zeros(numwords)

