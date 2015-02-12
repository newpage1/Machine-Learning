from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = difMat**2
    sqdistance = sqDiffMat.sum(axis=1)
    distance = sqdistance**0.5
    sorteddis = distance.argsort()
    classcount = {}
    for i in range(k):
	    votelable = labels[sorteddis[i]]
	    classcount[votelable] = classcount.get(votelable,0) + 1
    

