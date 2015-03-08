from numpy import *
from math import exp
from logistic import *
def classify(value,weights):
    x = sum(value*weights)
    prob = 1.0/(1+exp(-x))
    if prob>0.5:
	    return 1.0
    else:
	    return 0.0

def horsetest():
    frtrain = open('horseColicTraining.txt')
    frtest = open('horseColicTest.txt')
    trainset = list()
    labelset = list()
    for line in frtrain.readlines():
	    valuelist = line.strip().split('\t')
	    linearr = list()
	    for i in range(21):
		    linearr.append(float(valuelist[i]))
	    trainset.append(linearr)
	    labelset.append(float(valuelist[21]))
    weights = randomweight(trainset,labelset,500)
    print weights
    num = 0.0
    errorcount = 0
    for line in frtest.readlines():
	    num += 1.0
	    valuelist = line.strip().split('\t')
	    linearr = list()
	    for i in range(21):
		    linearr.append(float(valuelist[i]))
	    result = classify(linearr,weights)
	    if result != float(valuelist[21]):
		    errorcount += 1
    errorrate = float(errorcount)/num
    print 'the error rate is about:%f' %errorrate


    
    
