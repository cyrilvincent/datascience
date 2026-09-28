import numpy as np

print(np.__version__)

a1 = np.array([1, 2, 3.99, 4, 5, 6], dtype=np.float64)
print(a1.dtype)
a2 = a1.astype(np.int64)
print(a2)

a1 = np.array([1,2,3,4])
a2 = np.arange(4)
print(a1, a2)
print(a1 * a2)
print(np.cos(a1))

print(np.sum(a1), a1.sum())

print(a1.dtype, a1.ndim, a1.size, a1.shape)

a10 = np.arange(10) * 2
print(a10)
print(a10[2:7])
print(a10[2:7:2])
print(a10[2:-3])
print(a10[:-3])
print(a10[2:])
print(a10[2::2])
print(a10[7:2:-2])
