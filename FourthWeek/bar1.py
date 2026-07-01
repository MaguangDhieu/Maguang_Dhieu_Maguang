import matplotlib.pyplot as plt

x = ['Peter', 'John', 'Mary', 'Sarah', 'Tom']
y = [20, 14, 26, 18, 30]

plt.bar(x, y, color='b', label='Data points')
plt.xlabel('Names of people')
plt.ylabel('Age')
plt.title('Bar Plot showing age of different people')
plt.legend()
plt.show()