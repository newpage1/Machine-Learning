from numpy import *
import bayes
def test():
    """
    the probability reach 1 represent badness 
    """
    listpost,listclass = bayes.loaddataset()
    myvocablist = bayes.createlist(listpost)
    tmatrix = list()
    for doc in listpost:
	    vec = bayes.word2vec(myvocablist,doc)
	    tmatrix.append(vec)
    p0,p1,pa = bayes.train(tmatrix,listclass)
    testdoc1 = ['love','my','dalmation']
    testvec1 = bayes.word2vec(myvocablist,testdoc1)
    print testdoc1,'classify as :',bayes.classify(testvec1,p0,p1,pa)
    testdoc2 = ['stupid','love']
    testvec2 = bayes.word2vec(myvocablist,testdoc2)
    print testdoc2,'classify as :',bayes.classify(testvec2,p0,p1,pa)


