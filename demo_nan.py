import numpy as np

a1 = np.array([1,2,3,np.nan,5])
print(a1)
print(a1 + 1)
print(a1.mean())
print(np.nanmean(a1))