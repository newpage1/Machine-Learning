from numpy import *
import bayes
def test():
    listpost,listclass = bayes.loaddataset()
    myvocablist = bayes.createlist(listpost)
    tmatrix = list()
    for doc in listpost:
	    vec = bayes.word2vec(myvocablist,doc)
	    tmatrix.append(vec)
    return bayes.train(tmatrix,listclass)
    
