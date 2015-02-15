"""
MachineLearning
"""
from numpy import *
import operator

def createDataSet():
    """
    the dataset used for simply testing
    """	
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify(inX,dataSet,labels,k):
    """
    knn ag. to process the matrxi
    """
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqdistance = sqDiffMat.sum(axis=1)
    distance = sqdistance**0.5
    sorteddis = distance.argsort()
    classcount = {}
    for i in range(k):
	    votelable = labels[sorteddis[i]]
	    classcount[votelable] = classcount.get(votelable,0) + 1
    sortedclass = sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedclass[0][0]
    
def text2matrix(filename):
    """
    transfer the text to matrix
    """
    fr = open(filename)
    arraylines = fr.readlines()
    number = len(arraylines)
    returnMat = zeros((number,3))
    labelvector = list()
    index = 0
    for line in arraylines:
	    line = line.strip()
	    formatline = line.split('\t')
	    returnMat[index,:] = formatline[0:3]
	    labelvector.append(int(formatline[-1]))
	    index += 1
    return returnMat,labelvector

def autonorm(dataSet):
    """
    normalization
    """
    minvalue = dataSet.min(0)
    maxvalue = dataSet.max(0)
    ranges = maxvalue - minvalue
    norm = zeros(shape(dataSet))
    m = dataSet.shape[0]
    norm = dataSet - tile(minvalue,(m,1))
    norm = norm/tile(ranges,(m,1))
    return norm,ranges,minvalue

def datingtest():
    """
    test the dating dataset ,ratio = 0.1,simply choose the previous 10 percent data for testing ,choosing randomly maybe the normal way
    """
    ratio = 0.10
    datamat,label = text2matrix('datingTestSet2.txt')
    normmat,ranges,minvalue = autonorm(datamat)
    m = normmat.shape[0]
    testvector = int(m*ratio)
    errorcount = 0.0
    for i in range(testvector):
	    result = classify(normmat[i,:],normmat[testvector:m,:],label[testvector:m],3)
	    print "the classifier result :%d,the real answer :%d"%(result,label[i])
	    if result != label[i]:
		    errorcount += 1.0
    print "the total error rate is %f"%(errorcount/testvector)
 
