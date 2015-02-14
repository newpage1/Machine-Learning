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
    

