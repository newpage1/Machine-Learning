from kNN import *
from os import listdir
from numpy import *

"""
use knn ag. to test the handwriting image
"""

def image2vector(filename):
    """
    transgfer the image to vector
    """
    returnmat = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
	    linestr = fr.readline()
	    for j in range(32):
		    returnmat[0,32*i+j] = int(linestr[j])
    return returnmat

def handwritingtest():
    """
    test the handwriting image
    """
    labels = list()
    traininglist = listdir('digits/trainingDigits')
    m = len(traininglist)
    trainmat = zeros((m,1024))
    for i in range(m):
	    filename = traininglist[i]
	    imgnum = int(filename.split('_')[0])
	    labels.append(imgnum)
	    trainmat[i,:] = image2vector('digits/trainingDigits/%s'%filename)
    testlist = listdir('digits/testDigits')
    mtest = len(testlist)
    errorcount = 0.0
    for i in range(mtest):
	    filename = testlist[i]
	    imgnum = int(filename.split('_')[0])
	    vector = image2vector('digits/testDigits/%s'%filename)
	    result = classify(vector,trainmat,labels,3)
	    print "the classifier result is :%d,the real answer is %d"%(result,imgnum)
	    if result != imgnum :
		    errorcount += 1.0
    print "the total error rate is :%f" %(errorcount/mtest)

		    

