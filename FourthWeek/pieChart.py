import matplotlib.pyplot as plt


Activities = ['Coding', 'Design', 'Marketing', 'Development']
hours = [15, 30, 45, 10]

plt.pie(hours, labels=Activities, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Pie Chart showing Time Spent on Activities')
plt.savefig('pie_chart.png')  # Save the pie chart as an image file
plt.show()