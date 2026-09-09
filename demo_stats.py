import numpy as np

rnd = np.random.randint(0, 10000, 1000000)
print(rnd.mean(), rnd.std(), np.median(rnd), np.quantile(rnd, [0.1, 0.25, 0.5, 0.75, 0.9]))