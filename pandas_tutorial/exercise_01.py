import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from scipy.stats import ttest_ind

file_path = 'test.csv'
df = pd.read_csv(file_path)
df = df.iloc[:, 1:]
data_train = df.values
sales_trainset = data_train[:-20, 3].reshape(-1, 1)
sales_test = data_train[-20:, 3].reshape(-1, 1)

# 1. tv to sales
tv2sales_model = LinearRegression()
tv_trainset = data_train[:-20, 0].reshape(-1, 1)
t1, p1=ttest_ind(tv_trainset,sales_trainset)
print('tv-sales: t:{},p-value:{}'.format(t1[0], p1[0]))
tv_test = data_train[-20:, 0].reshape(-1, 1)
tv2sales_model.fit(tv_trainset, sales_trainset)

plt.subplot(1, 3, 1)
plt.scatter(tv_test, sales_test, c='r')
sale_pre1 = tv2sales_model.predict(tv_test)
plt.plot(tv_test, sale_pre1, linewidth=2)

# 2 radio to sales
radio2sales_model = LinearRegression()
radio_trainset = data_train[:-20, 1].reshape(-1, 1)
radio_test = data_train[-20:, 1].reshape(-1, 1)
radio2sales_model.fit(radio_trainset, sales_trainset)
plt.subplot(1, 3, 2)
plt.scatter(radio_test, sales_test, c='r')
sale_pre2 = radio2sales_model.predict(radio_test)
plt.plot(radio_test, sale_pre2, linewidth=2)

# 3 new to sales
news2sales_model = LinearRegression()
news_trainset = data_train[:-20, 2].reshape(-1, 1)
news_test = data_train[-20:, 2].reshape(-1, 1)
news2sales_model.fit(news_trainset, sales_trainset)
plt.subplot(1, 3, 3)
plt.scatter(news_test, sales_test, c='r')
sale_pre3 = radio2sales_model.predict(news_test)
plt.plot(news_test, sale_pre3, linewidth=2)


# 3 dimension example

# tv-radio to sales
fg2 = plt.figure(2)
ax2 = Axes3D(fg2)
tv_radio_train = data_train[:-20, 0:2]
tv_radio_test = data_train[-20:, 0:2]
tv_raido_model = LinearRegression()
tv_raido_model.fit(tv_radio_train, sales_trainset)
coef = tv_raido_model.coef_
intereption = tv_raido_model.intercept_
tv_x = np.squeeze(tv_radio_test[:, 0])
radio_y = np.squeeze(tv_radio_test[:, 1])
tv_X, radio_Y = np.meshgrid(tv_x, radio_y)
z = np.squeeze(sales_test)
ax2.scatter(tv_x, radio_y, z, c='black')
tv_radio_pre = tv_X*coef[0][0]+radio_Y*coef[0][1]+intereption[0]
ax2.plot_surface(tv_X, radio_Y, tv_radio_pre, cstride=1, rstride=1, cmap=plt.get_cmap('rainbow'))


# tv-new to sales
fg3 = plt.figure(3)
ax3 = Axes3D(fg3)
tv_new_train = data_train[:-20, [0, 2]]
tv_new_test = data_train[-20:, [0, 2]]
tv_new_model = LinearRegression()
tv_new_model.fit(tv_new_train, sales_trainset)
coef2 = tv_new_model.coef_
intereption2 = tv_new_model.intercept_
tv_x = np.squeeze(tv_new_test[:, 0])
new_y = np.squeeze(tv_new_test[:, 1])
tv_X, new_Y = np.meshgrid(tv_x, new_y)
z = np.squeeze(sales_test)
ax3.scatter(tv_x, new_y, z, c='black')
tv_new_pre = tv_X*coef2[0][0]+new_Y*coef2[0][1]+intereption2[0]
ax3.plot_surface(tv_X, new_Y, tv_new_pre, cstride=1, rstride=1, cmap=plt.get_cmap('rainbow'))



#  radio-new to sales
fg4 = plt.figure(4)
ax4 = Axes3D(fg4)
radio_new_train = data_train[:-20, [1, 2]]
radio_new_test = data_train[-20:, [1, 2]]
radio_new_model = LinearRegression()
radio_new_model.fit(radio_new_train, sales_trainset)
coef3 = radio_new_model.coef_
intereption3 = radio_new_model.intercept_
radio_x = np.squeeze(radio_new_test[:, 0])
new_y = np.squeeze(radio_new_test[:, 1])
radio_X, new_Y = np.meshgrid(radio_x, new_y)
z = np.squeeze(sales_test)
ax4.scatter(radio_x, new_y, z, c='black')
radio_new_pre = radio_X*coef3[0][0]+new_Y*coef3[0][1]+intereption3[0]
ax4.plot_surface(radio_X, new_Y, radio_new_pre, cstride=1, rstride=1, cmap=plt.get_cmap('rainbow'))


plt.show()