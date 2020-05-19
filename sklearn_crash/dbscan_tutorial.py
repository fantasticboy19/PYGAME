import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN

seed = np.random.seed(20)

data = np.random.randint(1, 100, (1000, 2))

dbscan = DBSCAN(eps=2)
index = dbscan.fit_predict(data)

color = list(set(index))
length = len(color)

plt.figure('dbscan')

plt.scatter(data[index == color[0], 0], data[index == color[0], 1], c='blue', marker='o', label='db_01')
plt.scatter(data[index == color[1], 0], data[index == color[1], 1], c='lightblue', marker='*', label='db_02')
plt.scatter(data[index == color[2], 0], data[index == color[2], 1], c='green', marker='v', label='db_03')
plt.scatter(data[index == color[3], 0], data[index == color[3], 1], c='yellow', marker='v', label='db_04')
plt.scatter(data[index == color[4], 0], data[index == color[4], 1], c='red', marker='o', label='db_05')
plt.scatter(data[index == color[5], 0], data[index == color[5], 1], c='black', marker='x', label="outlier")
