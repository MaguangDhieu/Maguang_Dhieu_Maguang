import matplotlib.pyplot as plt

x = [0, 2, 4, 8, 10]
y = [0, 4, 8, 16, 36]

plt.plot(x, y, marker='o', linestyle='--', color='b', label='Data points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with Markers and Custom Style')
plt.legend()
plt.grid()  
plt.show()