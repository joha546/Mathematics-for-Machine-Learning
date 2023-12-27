import numpy as np
import matplotlib.pyplot as plt

# Define vector v
v = np.array([-1, 2])

# Define vector i_hat as a transformed vector i_hat (ihat_t)
ihat_t = np.array([3, 1])

# Define vector j_hat as a transformed vector j_hat (jhat_t)
jhat_t = np.array([1, 2])

# Define v_ihat_t - vector v[0] (x) multiplied by transformed vector i_hat
v_ihat_t = v[0] * ihat_t

# Define v_jhat_t - vector v[1] (y) multiplied by transformed vector j_hat
v_jhat_t = v[1] * jhat_t

# Define transformed vector v (v_t) as vector v_ihat_t added to vector v_jhat_t
v_t = v_ihat_t + v_jhat_t

# Create a plot that graphically shows vector v (color='skyblue') transformed into
# transformed vector v (v_trfm - color='b') by adding v[0]*transformed vector ihat to v[1]*transformed vector jhat

# Create axes of the plot referenced as 'ax'
ax = plt.axes()

# Plot a red dot at the origin (0,0)
ax.plot(0, 0, 'or')

# Plot vector v_ihat_t as a dotted green arrow starting at the origin (0,0)
ax.arrow(0, 0, *v_ihat_t, color='g', linestyle='dotted', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plot vector v_jhat_t as a dotted red arrow starting at the origin defined by v_ihat_t
ax.arrow(v_ihat_t[0], v_ihat_t[1], *v_jhat_t, color='r', linestyle='dotted', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plot vector v as a blue arrow starting at the origin (0,0)
ax.arrow(0, 0, *v, color='skyblue', linewidth=2.5, head_width=0.30, head_length=0.35)

# Plot transformed vector v (v_t) as a blue colored vector (color='b) using the vector v's ax.arrow() statement as a template
ax.arrow(0, 0, *v_t, color='b', linewidth=2.5, head_width=0.30, head_length=0.35)

# Set limits for the x-axis
plt.xlim(-4, 4)

# Set major ticks for the x-axis
major_xticks = np.arange(-4, 4)
ax.set_xticks(major_xticks)

# Set limits for the y-axis
plt.ylim(-4, 4)

# Set major ticks for the y-axis
major_yticks = np.arange(-4, 4)
ax.set_yticks(major_yticks)

# Create gridlines for only major tick marks
plt.grid(b=True, which='major')

# Display the final plot
plt.show()
