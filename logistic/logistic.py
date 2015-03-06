from math import *
from numpy import *
import matplotlib.pyplot as plt

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

def plotfit():
    data,label = loaddataset()
    weights = weightcount(data,label)
    darray = array(data)
    n = darray.shape[0]
    x1cord = list(); y1cord = list()
    x2cord = list(); y2cord = list()
    for i in range(n):
	    if label[i] == 1:
		    x1cord.append(darray[i][1])
		    y1cord.append(darray[i][2])
	    else:
		    x2cord.append(darray[i][1])
		    y2cord.append(darray[i][2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x1cord,y1cord,s = 30,c = 'red',marker = 's')
    ax.scatter(x2cord,y2cord,s = 30,c = 'green')
    x = arange(-3.0,3.0,0.1)
    y = array((-weights[0]-weights[1]*x)/weights[2])
    x = mat(x).transpose()
    y = y.transpose()
    ax.plot(x,y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()
   # return x,y

