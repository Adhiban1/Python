import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(x)
def differentiate(x, y):
    if len(x) == len(y):
        x1 = []
        y1 = []
        for i in range(len(x)-1):
            x1.append((x[i+1]+x[i])/2)
            y1.append((y[i+1]-y[i])/(x[i+1]-x[i]))
        return (x1, y1)
    else:
        print("Error")
        return (0, 0)

dx, dy = differentiate(x, y)
d2x, d2y = differentiate(dx, dy)
d2x, d2y = np.array(d2x), np.array(d2y)
plt.plot(d2x, d2y)
plt.grid()
plt.show()