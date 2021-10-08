import numpy as np
import sys, time
import matplotlib.pyplot as plt
import math

c=np.loadtxt("./kyusyu_20211007.csv",delimiter=',')
a=c[0]

#x=range(len(a))
#plt.plot(x,a)
#plt.show()
#b=c[1]
#x=range(len(b))
#plt.plot(x,b)
#plt.show()

N=len(a)
L=math.floor(N/2)
K=N-L+1
xt=[[a[i+j]for j in range(L)] for i in range(K)]
Xt=np.array(xt,np.float64)
#print(type(Xt))
X=Xt.T
u, s, vh = np.linalg.svd(X, full_matrices=True)
