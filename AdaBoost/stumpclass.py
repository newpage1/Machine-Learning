from numpy import *
from math import log

def loadtest():
    D = mat(ones((5,1))/5)
    datamat = mat([[1.,2.1],[2.,1.1],[1.3,1.],[1.,1.],[2.,1.]])
    labelmat = [1.0,1.0,-1.0,-1.0,1.0]
    return datamat,labelmat,D

def stumpclass(datamat,dimension,threshold,ineq):
    retarr = ones((datamat.shape[0],1))
    if ineq == 'lt':
	    retarr[datamat[:,dimension]<=threshold] = -1.0
    else:
	    retarr[datamat[:,dimension]> threshold] = -1.0
    return retarr

def findbeststump(datamat,labelmat,D):
    """
    D represent the weight vector but don't need to process in this function
    """
    matrix = mat(datamat);label = mat(labelmat).transpose()#.transpose() and .T
    m,n = matrix.shape
    beststump = {};minerror = inf;bestclass = mat(zeros((m,1)));steps = 10.0#step length
    for i in range(n):
	    rangemin = matrix[:,i].min();rangemax = matrix[:,i].max()#min() and .min()
	    stepsize = (rangemax-rangemin)/steps
	    for j in range(-1,int(steps)+1):
		    threshold = rangemin + float(j)*stepsize
		    for ineq in ['lt','gt']:
			     predict = stumpclass(matrix,i,threshold,ineq)
			     #print predict
			     errvector = mat(ones((m,1)))
			     errvector[predict == label] = 0
			     #p = list(predict);l = list(label)
			     #p = [float(item) for item in p];l = [foat(item) for item in l]
			     #for k in range(m):
				    # if p[k] == l[k]:
					    # errvector[k] = 0
			     #print errvector
			     weightederror = D.T*errvector
			     print 'split:dimension:%d,threshold:%.2f,inequal:%s error rate:%.3f' %(i,threshold,ineq,weightederror)
			     if weightederror < minerror:
				     minerror = weightederror
				     bestclass = predict.copy()
				     beststump['dim'] = i
				     beststump['thre'] = threshold
				     beststump['ineq'] = ineq
    return beststump,minerror,bestclass

def adaboost(data,label,cycle=40):
    m = data.shape[0]
    d = mat(ones((m,1))/m)
    addclass = mat(zeros((m,1)))
    weakds = list()
    for i in range(cycle):
	    beststump,minerr,bestclass = findbeststump(data,label,d)
	    print 'D:',d.T
	    alpha = float(0.5*log((1.0-minerr)/max(minerr,1e-16)))
	    beststump['alpha'] = alpha
	    weakds.append(beststump)
	    print 'class:',bestclass.T
	    expvalue = multiply(-1*alpha*mat(label).T,bestclass)
	    d = multiply(d,exp(expvalue))
	    d = d/d.sum()
	    addclass += alpha*bestclass
	    print 'addedclass:',addclass.T
	    adderror = multiply(sign(addclass)!=mat(label).T,ones((m,1)))
	    error_rate = adderror.sum()/m
	    print 'error rate:',error_rate
	    if error_rate == 0.0: break
    return weakds


