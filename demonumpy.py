import numpy as np
print(np.__version__)

l1 = [1,2,3]
l2 = [4,5,6]
s = 3
print(l1+l2)

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(a1 + a2)
print(a1 + s)
print(3 * a1)

np.random.seed(0)
x1 = np.random.randint(10,size=6)
print(x1)
print(x1.ndim)
print(x1.size)
print(x1.shape)

predicate = x1 % 2 == 0
print(predicate)

print(x1[[True,True,False,True,True,True]])
x2 = x1[x1 % 2 == 0]
