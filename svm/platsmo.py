from numpy import *
from simplesvm import *

class optstruct:
def _init_(self,datamat,label,c,toler):
    self.X = datamat
    self.labelmat = label
    self.c= c
    self.tol = toler
    self.m = shape(datamat)[0]
    self.alpha = mat(zeros((self.m,1)))
    self.b = 0
    self.ecache = mat(zeros((self.m,2)))

def clacEk(oS,k):
    """
    T(w*label)*(D*D_k)+b
    """
    fxk = float(multiply(oS.alpha,oS.labelmat).T*(oS.X*oS.X[k,:].T))+oS.b
    ek = fxk - float(oS.labelmat[k])
    return ek

def selectJ(i,oS,Ei):
    maxk = -1;maxe = 0;ej = 0
    oS.ecache[i] = [1,Ei]
    cachelist = nonzero(oS.ecache[:,0].A)[0]
    if len(cachelist) > 1:
	    for k in cachelist:
		    if k==i : continue
		    ek = clacEk(oS,k)
		    deltae = abs(Ei-ek)
		    if deltae > maxe :
			    maxk = k;maxe = deltae;ej = ek
	    return maxk,ej
    else:
	    j = selectJrand(i,oS.m)
	    ej = calcEk(oS,j)
	    return j,ej
    
def updateEk(oS,k):
    ek = calcEk(oS,k)
    oS.ecache[k] = [1,ek]


