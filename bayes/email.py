from bayes import *
import re
import random

def preparedata(context):
    token = re.compile('\\w*')
    wordlist = token.split(context)
    tokenlist = list()
    for word in wordlist:
	    if len(word) > 0:
		    tokenlist.append(word.lower())
    return tokenlist

def emailtest():
    doclist = list()
    classlist = list()
    fulltext = list()
    for i in range(1,26):
	    wordlist = preparedata(open('email/spam/%d.txt' %i).read())
	    doclist.append(wordlist)
	    fulltext.extend(wordlist)
	    classlist.append(1)
	    wordlist = preparedata(open('email/ham/%d.txt' %i).read())
	    doclist.append(wordlist)
	    fulltext.extend(wordlist)
	    classlist.append(0)
    vocablist = createlist(doclist)
    trainset = range(50)
    testset = list()
    for i in range(10):
	    randindex = int(random.uniform(0,len(trainset)))
	    testset.append(trainset[randindex])
	    del(trainset[randindex])
    tmatrix = list()
    trainclass = list()
    for index in trainset:
	    tmatrix.append(word2vec(vocablist,doclist[index]))
	    trainclass.append(classlist[index])
    p0,p1,pa = train(tmatrix,trainclass)
    errorcount = 0.0
    for index in testset:
	    testvec = word2vec(vocablist,doclist[index])
	    if classify(testvec,p0,p1,pa) != classlist[index]:
		    errorcount += 1
    print "the error rate is about %f" %(errorcount/len(testset))



