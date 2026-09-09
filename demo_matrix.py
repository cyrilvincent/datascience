import numpy as np

m23 = np.array([[1,2,3],[4,5,6]])
print(m23)
print(m23[1,2])
print(m23 * 2)
print(np.cos(m23))
print(np.max(m23))
m23[1,1] = m23[1,1] * 2
print(m23)

print(m23.ndim, m23.shape, m23.size)  # numpy row first

v12 = np.arange(12)
m34 = v12.reshape(3,4)
m43 = v12.reshape(4,3)

print(v12)
print(m34)
print(m43)
print(m34.reshape(12))