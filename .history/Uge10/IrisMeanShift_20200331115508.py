import pandas as pd
import numpy as np
# iris_data = pd.read_csv('iris_data.csv')
iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data)

iris_data_Species = pd.get_dummies(iris_data, columns=['Species'])

print(iris_data_Species)