
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
  
fig = plt.figure()
  
ax1 = fig.add_subplot(111, projection='3d')
  
u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]

x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
  
ax1.plot_wireframe(x, y, z, rstride = 6, cstride = 6, linewidth = 2)
  
plt.show()
