import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(1.0)

x = r*np.cos(theta)
y = r*np.sin(theta)

fig, ax = plt.subplots(1)

ax.plot(x, y)
ax.set_aspect(1)
plt.show()
