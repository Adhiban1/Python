import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)
dy = []
for i in range(len(y)-1):
    dy.append(float((y[i+1]-y[i])/(x[i+1]-x[i])))
dy.append(dy[-1])
plt.plot(x, y)
plt.plot(x, dy)
plt.grid()
plt.show()