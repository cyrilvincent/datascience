import matplotlib.pyplot as plt
import numpy as np

a1 = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
asin = np.sin(a1)
acos = np.cos(a1)
atanh = np.tanh(a1)

plt.title("sin(x)")
plt.subplot(2, 2, 1)
plt.plot(a1, asin, color="red", label="sin")
plt.scatter(a1, acos, color="blue", label="cos")
plt.legend()
plt.subplot(2, 2, 2)
plt.plot(a1, atanh, color="red", label="sin")
plt.subplot(2, 2, 3)
a2 = np.arange(0,5)
plt.bar(a2, a2)
plt.savefig("demo.png")
plt.show()
