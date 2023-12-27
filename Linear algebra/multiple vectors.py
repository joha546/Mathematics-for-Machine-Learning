import numpy as np
import matplotlib.pyplot as plt

# Meshgrid
x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

# Directional Vectors
u= -y/np.sqrt(x**2 + y**2)
v= x/(x**2 + y**2)

# Plotting vector field using quiver
plt.quiver(x,y,u,v, color='g')
plt.title("Vector Field")

# Setting limits
plt.xlim(-7,7)
plt.ylim(-7,7)

plt.grid()
plt.show()