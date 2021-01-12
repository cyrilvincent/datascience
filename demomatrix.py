import numpy as np

m1 = np.array([[1,2],[3,4]])
print(m1)
print(m1 ** 2)
f = lambda x : x * np.sin(x)
print(f(m1))
print(m1.shape, m1.ndim, m1.size) #Row first

v1 = np.array([5,6,7,8])
m2 = v1.reshape(2,-1) #Idem (2,2) ou (-1,2) #Row first
print(m2)
print(m2.T)
print(m1 + m2)
print(m1 * m2)
print(m1.dot(m2))

print(m1.sum())
print(np.sum(m1, axis=1))