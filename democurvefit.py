import numpy as np
import random

noise = 0
def f(x):
    delta = (random.random() - 0.5) * noise
    return  (2.5 + delta) * x * np.sin(x * (0.7 + delta)) + 2 + delta # f(x) = 2.5x sin(0.7x) + 2

x_plot = np.linspace(0, 10, 100)
x = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
rng.shuffle(x)
x = np.sort(x[:20])
y = f(x)
X = x[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]

import matplotlib.pyplot as plt
plt.scatter(x_plot, f(x_plot))
plt.show()

g = lambda x, a, b, c: a * x * np.sin(x * b) + c

import scipy.optimize as opt
print(x.shape)
print(y.shape)
weigths, conv = opt.curve_fit(g, x, y)
print(weigths)
print(conv)



