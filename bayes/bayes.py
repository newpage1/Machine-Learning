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
    for word in inputset:
	    if word in vocablist:
		    returnvec[vocablist.index(word)] = 1
	    else:
		    print "%s is not in the vocabulary" %word
    return returnvec

def train(tmatrix,category):
    numdocs = len(tmatrix)
    numwords = len(tmatrix[0])
    pa = sum(category)/float(numdocs)
    p0num = zeros(numwords)
    p1num = zeros(numwords)
    p0 = 0.0
    p1 = 0.0
    for i in range(numdocs):
	    if category[i] == 1:
		    p1num += tmatrix[i]
		    p1 += sum(tmatrix[i])
	    else:
		    p0num += tmatrix[i]
		    p0 += sum(tmatrix[i])
    p1vec = p1num/p1
    p0vec = p0num/p0
    return p1vec,p0vec,pa

def loaddataset():
    vocablist = [['my','dog','has','flea','problems','help','please'],['maybe','not','take','him','to','dog','park','stupid'],['my','delamation','is','so','cute','i','love','him'],['stop','posting','stupid','worthless','garbage'],['mr','licks','ate','my','steak','how','to','stop','hime'],['quit','buying','worthless','dog','food','stupid']]
    classvec = [0,1,0,1,0,1]
    return vocablist,classvec
