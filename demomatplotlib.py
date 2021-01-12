import matplotlib.pyplot as plt
import matplotlib
import numpy as np

print(matplotlib.__version__)

#plt.subplot(121)
x = np.linspace(-10, 10, 100)
f = lambda x: 0.5 + 0.5 * np.tanh(x / 2)
y = f(x)
plt.plot(x, y)

#plt.subplot(122)
sigmoidfn = lambda x: 1 / (1 + np.exp(-x))
plt.plot(x, sigmoidfn(x))
plt.show()

#tanhFn = lambda x: 0.5 + 0.5 * math.tanh(x / 2)

# Afficher la courbe sigmoide et tanh