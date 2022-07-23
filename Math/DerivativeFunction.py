import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
y1 = np.cos(x)
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
dx, dy = np.array(dx), np.array(dy)+0.05
plt.plot(dx, dy)
plt.plot(x, y1)
plt.grid()
plt.show()