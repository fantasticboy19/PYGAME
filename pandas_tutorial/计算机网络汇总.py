import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from scipy.stats import ttest_ind
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 获得数据，并可视化查看feature之间的联系
data = pd.read_csv('Default.csv', usecols=['balance', 'income', 'student', 'default'])
# sns.pairplot(data=data, hue='student')

def logistic_classifier(data):
    data.loc[data['student'] == 'Yes', ['student']] = 1
    data.loc[data['student'] == 'No', ['student']] = 0
    data.loc[data['default'] == 'Yes', ['default']] = 1
    data.loc[data['default'] == 'No', ['default']] = 0
    # print(data[['Rating', 'Income']])
    classifier_1 = LogisticRegression()
    data = data.values
    x_train = data[:-30, [1, 2, 3]]
    x_test = data[-30:, [1, 2, 3]]
    y_train = data[:-30, 0]
    y_test = data[-30:, 0]
    # print(x_train, y_test)
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    # print(x_train[:5], y_train[:5])
    #
    # print(y_train.shape, type(y_train))
    # print(y_train)
    classifier_1.fit(x_train, y_train.astype('int'))
    # print('classifier parameters are student:{},balance:{},income:{},bias:{}'.format(classifier_1))
    # classifier_1.score(x_test, y_test)
    result = classifier_1.score(x_test, y_test.astype('int'))
    # print(result, y_test)

    print(f'r2 is {result}, and the logistic_classifier parameters are {classifier_1.coef_} and {classifier_1.intercept_}')
# print(data.head())
# sns.lineplot(data=data)
#
# sns.set(style='whitegrid')
# data = pd.read_csv('tips.csv')
#
# # sns.relplot(x="total_bill", y="tip",data=data, hue='day', )

# solution 1 to use seaborn to make a pairplot

# # g = sns.PairGrid(data=data, hue="size", palette="GnBu_d")
# # g.map(plt.scatter, s=50, edgecolor="white")
# # g.add_legend()

# 方法2 直接使用pairplot函数进行绘图
# sns.pairplot(data=data, hue='Student')
    # visualize the boundary of the logisticRegression
    fig = plt.figure('logisticRegression boundary plane')
    ax = Axes3D(fig)
    student = x_test[:, 0]
    balance = x_test[:, 1]
    income = x_test[:, 2]
    ax.scatter(student, balance, income, c=y_test)
    student_n, balance_n = np.meshgrid(student, balance)
    income_n = (classifier_1.coef_[0][0]*student_n + classifier_1.coef_[0][1]*balance_n+classifier_1.intercept_)/(-classifier_1.coef_[0][2])
    ax.plot_surface(student_n, balance_n, income_n, cstride=1, rstride=1, cmap=plt.get_cmap('rainbow'))


def lda_classifier(data):
    data.loc[data['student'] == 'Yes', ['student']] = 1
    data.loc[data['student'] == 'No', ['student']] = 0

    data.loc[data['default'] == 'Yes', ['default']] = 1
    data.loc[data['default'] == 'No', ['default']] = 0
    # print(data[['Rating', 'Income']])
    data = data.values
    x_train = data[:-30, [1, 2, 3]]
    x_test = data[-30:, [1, 2, 3]]
    y_train = data[:-30, 0].astype('int')
    y_test = data[-30:, 0].astype('int')
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    # x_train = data[:, [1, 2, 3]]
    # y_train = data[:, 0].astype('int')
    lda = LDA(n_components=1)
    x_train_lda = lda.fit_transform(x_train, y_train)
    x_test_lda = lda.transform(x_test)
    print(
        x_train_lda
    )
    lda.fit(x_train_lda, y_train)
    # x_train_lda = lda.fit_transform(x_train, y_train)
    # return x_train_lda, y_train
    y_pre = lda.predict(x_test_lda)
    score = lda.score(x_test_lda, y_test)
    return x_test_lda, y_pre, y_test

if __name__ == '__main__':
    logistic_classifier(data)
    x, y_pre, y = lda_classifier(data)
    length = x.shape[0]
    plt.figure('lda分类器：上面是预测的，下面是gt')
    plt.subplot(2, 1, 1)
    plt.scatter(x, [0]*length, c=y_pre)

    plt.subplot(2, 1, 2)
    plt.scatter(x, [0]*length, c=y)
    plt.show()

