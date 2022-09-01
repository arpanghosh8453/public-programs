import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5,5,0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y)
plt.plot(x,z)
plt.grid()
plt.show()
