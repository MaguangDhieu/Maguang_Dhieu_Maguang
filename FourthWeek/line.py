import matplotlib.pyplot as plt
import numpy as np  

x = np.linspace(0, 10, 100)
y = 2 * x + 1

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()