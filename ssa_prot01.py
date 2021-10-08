import numpy as np
import sys, time
import matplotlib.pyplot as plt
import math

def sn(xx):
# {i, j, k, n, n1, x, sum}, x = {};print(Xt.shape[0]);print(Xt.shape[1])
  x=np.empty(0)
  n1=xx.shape[0];n=xx.shape[1]
  j=0;sum=0
  for i in range(1,n1+1):
    for k in range(1,i+1):
      if k< n :
        sum=sum+xx[i-k+1-1,k-1]
        j=j+1
    x=np.append(x,sum/j)
    j=0;sum=0
  for i in range(2,n+1):
    for k in range(1,n-i+1+1):
      if k< n1 :
        sum=sum+xx[n1-k+1-1,k+i-1-1]
        j=j+1
    x=np.append(x,sum/j)
    sum=0;j=1 
  return x  

c=np.loadtxt(sys.argv[1],delimiter=',')
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
#print(Xt.shape)
X=Xt.T
u, s, vh = np.linalg.svd(X, full_matrices=True)
xx=np.matmul((u.T)[0].reshape(-1,1),((vh.T)[0]).reshape(1,-1))
print(((u.T)[0]).reshape(-1,1).shape)
print(((vh.T)[0]).reshape(1,-1).shape)
x=sn(xx)
#print(x)
xn=range(len(x))
plt.plot(xn,x)
plt.show()