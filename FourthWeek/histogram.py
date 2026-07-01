import matplotlib.pyplot as plt


sizes = [15, 30, 45, 10, 20, 25, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

plt.hist(sizes,  bins=4, color='b', edgecolor='black', alpha=0.7)
plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.legend()
plt.show()
