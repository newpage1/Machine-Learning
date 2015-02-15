"""
decision tree
"""
from math import log
import operator

def entropy(dataSet):
    """
    calculate the shanon entropy with the last column
    """
    num = len(dataSet)
    label = {}
    for vector in dataSet:
	    currentlabel = vector[-1]
	    if currentlabel not in label.keys():
		    label[currentlabel] = 0
	    label[currentlabel] += 1
    ent = 0.0
    for key in label.keys():
	    prob = float(label[key])/num
	    ent -= prob*log(prob,2)
    return ent

def splitSet(dataSet,axis,value): 
    """
    use the axis to split the dataset
    """
    resultset = list()
    for vector in dataSet:
	    if vector[axis] == value:
		    splitvector = vector[:axis]
		    splitvector.extend(vector[axis+1:])
		    resultset.append(splitvector)
    return resultset

def bestaxis(dataSet):
    """
    use the shanon entropy to choose the best axis feature
    """
    num = len(dataSet[0]) - 1
    baseent = entropy(dataSet)
    bestentropy = 0.0
    bestfeature = -1
    for i in range(num):
	    fealist = [example[i] for example in dataSet]
	    ivalue = set(fealist)
	    newentropy = 0.0
	    for value in ivalue:
		    subDataSet = splitSet(dataSet,i,value)
		    prob = len(subDataSet)/float(len(dataSet))
		    newentropy += prob*entropy(subDataSet)
	    infogain = baseent - newentropy
	    if infogain > bestentropy :
		    bestentropy = infogain
		    bestfeature = i
    return bestfeature

def majoritycnt(classlist):
    """
    vote for the highest feature
    """
    classcount = {}
    for vote in classlist:
	    if vote not in classcount.keys():
		    classcount[vote] = 0
	    classcount[vote] += 1
    sortedclass = sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse = True)
    return sortedclass[0][0]

def createtree(dataSet,labels):
    """
    recurrence to create the tree
    """
    classlist = [example[-1] for example in dataSet]
    if classlist.count(classlist[0]) == len(classlist):
	    return classlist[0]
    if len(dataSet[0]) == 1:
	    return majoritycnt(classlist)
    bestfeature = bestaxis(dataSet)
    bestlabel = labels[bestfeature]
    mytree = {bestlabel:{}}
    del(labels[bestfeature])
    feavalues = [example[bestfeature] for example in dataSet]
    vals = set(feavalues)
    for value in vals:
	    sublabel = labels[:]
	    mytree[bestlabel][value] = createtree(splitSet(dataSet,bestfeature,value),sublabel)
    return mytree
    
def createset():
    dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
    labels = ['no swimming','flipper']
    return dataSet,labels

