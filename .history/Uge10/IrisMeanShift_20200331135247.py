import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle

# 1.
# iris_data = pd.read_csv('iris_data.csv')
iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data)

# 2.
iris_data_Species = pd.get_dummies(iris_data, columns=['Species'])
print(iris_data_Species)

# 3.

# iris_data.plot.scatter(x=0 , y=1)
# plt.show()

virginica = iris_data.loc[iris_data['Species_I. virginica'] == 1]
plt.show()

# Plot
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.title('Scatter plot pythonspot.com')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

