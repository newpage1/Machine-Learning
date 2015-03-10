from numpy import *
import random
def loaddataset(filename):
    datamat = list()
    labelmat = list()
    fr = open(filename)
    for line in fr.readlines():
	    valuelist = line.strip().split('\t')
	    datamat.append([float(valuelist[0]),float(valuelist[1])])
	    labelmat.append(float(valuelist[2]))
    return datamat,labelmat

def selectj(i,m):
    j = i
    while j == i:
	    j = int(random.uniform(0,m))
    return j

def clipalf(axi,H,L):
    if axi > H:
	    axi = H
    if axi < L:
	    axi = L
    return axi

def simplesmo(datamatin,labelmatin,c,toler,maxiter):
    datamat = mat(datamatin)
    labelmat = mat(labelmatin).transpose()
    b = 0
    m,n = shape(datamat)
    alpha = mat(zero((m,1)))
    iternum = 0
    while iternum < maxiter:
	    changeflag = 0
	    for i in range(m):
		    fxi = float(multiply(alpha,labelmat).T*datamat*datamat[i,:].T) + b
		    ei = fxi - float(labelmat[i])
		    if ((labelmat[i]*ei < -toler and alpha[i] < c ) or (labelmat[i]*ei > toler and alpha[i] >0)):
			    j = selectj(i,m)
			    fxj = float(multiply(alpha,labelmat).T*datamat*datamat[j,:].T) + b
			    ej = fxj - float(labelmat[j])
			    oldi = alpha[i].copy()
			    oldj = alpha[j].copy()
			    if alpha[i] != alpha[j]:
				    L = max(0,alpha[j]-alpha[i])
				    H = min(c,c+alpha[j]-alpha[i])
			    else:
				    L = max(0,alpha[i]+alpha[j]-c)
				    H = min(c,alpha[i]+alpha[j])
			    if L==H:
				    print 'L = H'
				    continue
			    eta = 2.0*datamat[i,:]*datamat[j,:] - datamat[i,:]*datamat[i,:] - datamat[j,:]*datamat[j,:]
			    if eta >= 0:
				    print 'eta >= 0'
				    continue
			    alpha[j] -= labelmat[j]*(ei - ej)/eta
			    alpha[j] = clipalf(alpha[j],H,L)
			    if(abs(alpha[j]-oldj)<0.0001)
				    print 'not moving enough'
				    continue







    

