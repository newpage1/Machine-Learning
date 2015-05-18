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
    cachelist = nonzero(oS.ecache[:,0].A)[0]#return the nonzero number index tuple list of the NO.0 row of the matrix 
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

def innerL(i,os):
    ei = calcEk(os,i)
    if (os.labelmat[i]*ei < -os.tol and os.alpha[i]< c) or (os.labelmat[i]*ei >os.tol and os.alpha[i] > 0):
	    j,ej = selectJ(i,os,ei)
	    iold = os.alpha[i].copy()
	    jold = os.alpha[j].copy()
	    if os.labelmat[i] != os.labelmat[j]:
		    L = max(0,os.alpha[j] - os.alpha[i])
		    H = min(os.c,os.c + os.alpha[j] - os.alpha[i])
	    else:
		    L = max(0,os.alpha[i] + os.alpha[j] - os.c)
		    H = min(os.c,os.alpha[i] + os.alpha[j])
	    if L==H:
		    print 'L=H';return 0
	    eta = 2.0*os.X[i,:]*os.X[j,:].T - os.X[i,:]*os.X[i,:].T - os.X[j,:]*os.X[j,:].T
	    if eta > 0:
		    print 'eta>0';return 0
	    os.alpha[j] -= os.labelmat[j]*(ei-ej)/eta
	    os.plpha[j] = clipAlpha(os.alpha[j],H,L)
	    updateEk(os,j)
	    if abs(os.alpha[j] - jold) < 0.00001:
		    print 'j not moving enogh';return 0
	    os.alpha[i] += os.labelmat[j]*os.labelmat[i]*(jold - os.alpha[j])
	    updateEk(os,i)
	    b1 = os.b - ei - os.labelmat[i]*(os.alpha[i] - iold)*(os.X[i,:]*os.X[i,:].T) - os.labelmat[j]*(os.alpha[j] - jold)*(os.X[i,:]*os.X[j,:].T)
	    b2 = os.b - ej - os.labelmat[i]*(os.alpha[i] - iold)*(os.X[i,:]*os.X[j,:].T) - os.labelmat[j]*(os.alpha[j] - jold)*(os.X[j,:]*os.X[j,:].T)
	    if os.alpha[i] > 0 and os.alpha[i] < os.c:
		    os.b = b1
		    elif os.alpha[j] > 0 and os.alpha[j] < os.c:
			    os.b = b2
		    else:
			    os.b = (b1+b2)/2.0
		    return 1
    else:
	    return 0

def smop(datamat,classlabel,c,tol,maxiter,ktup=('lin',0)):
    os = optstruct(mat(datmat),mat(classlabel).tanspose(),c,tol)
    iter = 0;entire = True;pairchange = 0
    while iter < maxiter and pairchange >0 or entire:
	    pairchange = 0
	    if entire:
		    for i in range(os.m):
			    pairchange += innerL(i,os)
		    print 'full set ,iter:%d,i:%d,pairchange:%d' %(iter,i,pairchange)
		    iter += 1
	    else:
		    nonbound = nonzero((os.alpha.A>0)*(os.alpha.A<c))[0]
		    for i in nonbound:
			    pairchange += innerL(i,os)
		    print 'nonbound ,iter:%d,i:%d,pairchange:%d' %(iter,i,pairchange)
		    iter +=1
	    if entire:
		    entire = False
	    elif pairchange == 0 :
		    entire = True
	    print 'iteration number:%d' %iter
    return os.b,os.alpha
	

