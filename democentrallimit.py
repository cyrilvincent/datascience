import numpy as np
import matplotlib.pyplot as plt

nb = 1000
#np.random.seed(0)
mat = np.random.rand(nb,nb)
sums = mat.sum(axis=1)
print(sums)
plt.bar(np.arange(nb), sums)
plt.show()

x = np.arange(-100,100)
mu = 0
sigma = 20
f = lambda x : 1/(np.sqrt(2*np.pi*pow(sigma,2))) * np.exp(-pow((x-mu),2)/(2*pow(sigma,2)))
plt.plot(x, f(x))
plt.show()