import numpy as np

print(np.__version__)

a1 = np.array([1,2,3,4,5,6,7], dtype=np.float64)
a2 = np.arange(7, dtype=np.float64)

print(a1)
print(a2)

a3 = a1 + a2
print(a3)

print(a1 * 2 + 1 + np.cos(a2))

x = 3.9999
print(np.round(x, 0))
a4 = a1 - 0.555
print(a4)
print(np.round(a4,1))

print(np.random.randint(0,100,10))

print(np.sum(a1), a1.sum())

print(np.ndim(a1), a1.shape, a1.size, a1.dtype)

a5 = np.array([0,1,254,255], np.uint8)
print(a5 + 1)
print(a5 - 1)
