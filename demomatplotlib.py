import matplotlib.pyplot as plt
import matplotlib
import numpy as np

print(matplotlib.__version__)

plt.subplot(121)
x = np.linspace(0, 6*np.pi,100)
f = lambda x: 1 / x * np.sin(x)
y = f(x)
plt.plot(x, y)

plt.subplot(122)
x = np.linspace(-10, 10,100)
sigmoidfn = lambda x: 1 / (1 + np.exp(-x))
plt.plot(x, sigmoidfn(x))
plt.show()