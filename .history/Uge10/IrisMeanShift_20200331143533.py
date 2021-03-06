import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

# 1.
# iris_data = pd.read_csv('iris_data.csv')
iris_data = pd.read_excel('iris_data.xlsx')
# print(iris_data)

# 2.
iris_data = pd.get_dummies(iris_data, columns=['Species'])
# print(iris_data)

# 3.
virginica = iris_data.loc[iris_data['Species_I. virginica']==1]
versicolor = iris_data.loc[iris_data['Species_I. versicolor']==1]
setosa = iris_data.loc[iris_data['Species_I. setosa']==1]


# virginica.plot.scatter(x=0, y=1, c='r')
# versicolor.plot.scatter(x=0, y=1, c='b')
# setosa.plot.scatter(x=0, y=1, c='g')

plt.scatter(x=virginica['Sepal length'], y=virginica['Sepal width'], color='r')
plt.scatter(x=versicolor['Sepal length'], y=versicolor['Sepal width'], color='g')
plt.scatter(x=setosa['Sepal length'], y=setosa['Sepal width'], color='b')
# plt.show()

# 4.
print(estimate_bandwidth(iris_data, quantile=0.2))
analyzer = MeanShift(bandwidth=1)
print('Self MeanShift: ', analyzer.fit(iris_data))
print('Function mean_shift: ', mean_shift(iris_data))
# print(estimate_bandwidth(virginica, quantile=0.2))
# print(estimate_bandwidth(versicolor, quantile=0.2))
# print(estimate_bandwidth(setosa, quantile=0.2))

