import matplotlib.pyplot as plt

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 19, 23, 25, 27, 26, 21, 23, 20, 22, 24, 26, 25]


plt.scatter(day, temperature, color='r', marker='o')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Scatter Plot Example')
plt.show()

