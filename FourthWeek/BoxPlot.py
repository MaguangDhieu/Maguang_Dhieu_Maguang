import matplotlib.pyplot as plt

data = [[1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
        [3, 4, 5, 6, 7],
        [4, 5, 6, 7, 8]]

plt.boxplot(data)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Box Plot Example')
plt.show()