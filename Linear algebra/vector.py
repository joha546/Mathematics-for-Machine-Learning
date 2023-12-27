
'''
Plotting a single vector using quiver() method in matplotlib module.
'''
import numpy as np
import matplotlib.pyplot as plt

# vector origin location
X=[0]
Y=[0]

# Directional vectors
U=[2]
V=[3]

# Creating plot
plt.quiver(X,Y,U,V, color ='b', units='xy', scale=1)
plt.title("Single Vector")

# x-lim and y-lim
plt.xlim(-2,5)
plt.ylim(-2,3.5)

# show plot grid
plt.grid()
plt.show()