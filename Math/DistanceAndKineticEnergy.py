import numpy as np
import matplotlib.pyplot as plt

y = [0]
n = 100 -1
for i in range(n):
    y.append(y[i] + np.random.randint(1, 101))
x = np.arange(1, n + 2)
x1 = []
y1 = []
for i in range(len(x)-1):
    x1.append((x[i+1]+x[i])/2)
    y1.append((1/2)*((y[i+1]-y[i])/(x[i+1]-x[i]))**2)
print(sum(y1))
fig, axes = plt.subplots(2)
axes[0].plot(x, y)
axes[1].plot(x1,y1)
plt.show()