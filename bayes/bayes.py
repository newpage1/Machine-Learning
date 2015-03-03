from numpy import *
from math import log
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
    """
    0 represent the normal,and 1 represent the bad opinion
    """
    numdocs = len(tmatrix)
    numwords = len(tmatrix[0])
    pa = sum(category)/float(numdocs)
    p0num = ones(numwords)
    p1num = ones(numwords)
    p0 = 2.0
    p1 = 2.0
    for i in range(numdocs):
	    if category[i] == 1:
		    p1num += tmatrix[i]
		    p1 += sum(tmatrix[i])
	    else:
		    p0num += tmatrix[i]
		    p0 += sum(tmatrix[i])
    p1vec = p1num/p1
    p0vec = p0num/p0
    p0len = len(p0vec)
    p1len = len(p1vec)
    for i in range(p0len):
	    p0vec[i] = log(p0vec[i])
    for j in range(p1len):
	    p1vec[j] = log(p1vec[j])
    return p0vec,p1vec,pa


def loaddataset():
    vocablist = [['my','dog','has','flea','problems','help','please'],['maybe','not','take','him','to','dog','park','stupid'],['my','delamation','is','so','cute','i','love','him'],['stop','posting','stupid','worthless','garbage'],['mr','licks','ate','my','steak','how','to','stop','hime'],['quit','buying','worthless','dog','food','stupid']]
    classvec = [0,1,0,1,0,1]
    return vocablist,classvec

def classify(veclass,p0vec,p1vec,pa):
    p1 = sum(veclass*p1vec) + log(pa)
    p0 = sum(veclass*p0vec) + log(1-pa)
    if p1>p0 :
	    return 1
    else:
	    return 0

def bagofword(vocablist,inputset):
    returnvec = [0]*len(vocablist)
    for word in inputset:
	    if word in vocablist:
		    returnvec[vocablist.index(word)] += 1
	    else:
		    print "%s is not in the vocabulary" %word
    return returnvec

