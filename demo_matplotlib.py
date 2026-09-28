import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 2, 1)
plt.title("Trigo")
plt.plot(x, y, label="sin")
plt.scatter(x, y2, label="cos", color="red")
plt.legend()
plt.subplot(2, 2, 4)
xbar = np.arange(5)
ybar = 2 * xbar
plt.bar(xbar, ybar)
plt.show()
plt.bar(xbar, ybar)
plt.show()

