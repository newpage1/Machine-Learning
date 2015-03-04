from math import *
from numpy import *

def sigmoid(matrix):
    m,n = shape(matrix)
    for i in range(m):
	    for j in range(n):
		    matrix[i][j] = 1.0/(1+exp(-matrix[i][j]))
    return matrix

def loaddataset():
    datamat = list()
    labelmat = list()
    fr = open('testSet.txt')
    for line in fr.readlines():
	    linelist = line.strip().split()
	    datamat.append([1.0,float(linelist[0]),float(linelist[1])])
	    labelmat.append(int(linelist[-1]))
    return datamat,labelmat

def weightcount(datamat,labelmat):
    axi = 0.001
    dmatrix = mat(datamat)
    labelmat = mat(labelmat).transpose()
    cycle = 500
    n = dmatrix.shape[1]
    weights = ones((n,1))
    for i in range(cycle):
	    h = sigmoid(dmatrix*weights)
	    error = labelmat - h
	    weights = weights + axi*(dmatrix.transpose()*error)
    return weights


