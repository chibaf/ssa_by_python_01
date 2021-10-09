import numpy as np
import sys
import matplotlib.pyplot as plt

a=np.loadtxt(sys.argv[1],delimiter=',')
x=range(len(a))
plt.plot(x,a)
plt.show()

exit()