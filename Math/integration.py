import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3*np.pi, 10000)
y = np.sin(x)
area = 0
for i in range(len(y)-1):
    area += float((1/2)*(x[i+1]-x[i])*abs(y[i+1]-y[i])+min(y[i+1], y[i])*(x[i+1]-x[i]))
print(f'Area: {round(area, 5)}')
plt.plot(x, y)
plt.grid()
plt.show()