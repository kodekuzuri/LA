#(c)
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)


x = np.cos(theta) + 0.9*np.sin(theta)
y =  0.8*np.sin(theta) + 0.9*np.cos(theta)

fig, ax = plt.subplots(1)

ax.plot(x, y)
ax.set_aspect(1)
plt.show()

#(d)
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

x = np.cos(theta) 
y = -10*np.sin(theta) 

fig, ax = plt.subplots(1)

ax.plot(x, y)
ax.set_aspect(1)
plt.show()


#(e)
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

epsn = [10, 5, 1 , 1e-1, 1e-2, 1e-4, 0]

for i in epsn:
  x = np.cos(theta) + np.sin(theta)
  y = np.cos(theta) + i*np.sin(theta)

  fig, ax = plt.subplots(1)

  ax.plot(x, y)
  ax.set_aspect(1)
  plt.show()