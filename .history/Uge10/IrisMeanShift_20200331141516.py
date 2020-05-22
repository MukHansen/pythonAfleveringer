import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.
# iris_data = pd.read_csv('iris_data.csv')
iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data)

# 2.
iris_data = pd.get_dummies(iris_data, columns=['Species'])
print(iris_data)

# 3.

# iris_data.plot.scatter(x=0 , y=1)
# plt.show()

virginica = iris_data.loc[iris_data['Species_I. virginica']==1]
versicolor = iris_data.loc[iris_data['Species_I. versicolor']==1]
setosa = iris_data.loc[iris_data['Species_I. setosa']==1]


# virginica.plot.scatter(x=0, y=1, c='r')
# versicolor.plot.scatter(x=0, y=1, c='b')
# setosa.plot.scatter(x=0, y=1, c='g')
# plt.show()

x = range(100)
y = range(100,200)
fig = plt.figure()
ax1 = fig.add_subplot(333)

ax1.scatter(x[:4], y[:4], s=10, c='b', marker="s", label='first')
ax1.scatter(x[40:],y[40:], s=10, c='r', marker="o", label='second')
plt.legend(loc='upper left')
plt.show()


# Plot
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

