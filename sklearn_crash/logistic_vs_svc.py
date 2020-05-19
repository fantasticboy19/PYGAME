from sklearn.datasets import load_iris, load_wine
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

from sklearn.kernel_approximation import RBFSampler, Nystroem, AdditiveChi2Sampler, SkewedChi2Sampler

# raw_data = load_iris()
raw_data = load_wine()
data = raw_data['data']
# 150 * 4
target = raw_data['target']
# print(raw_data['target_names'])

total_data = np.c_[data, target]
# print(total_data.shape) 150 * 5

# # start to generate the initial data with 2 features and 2 classes
# print(raw_data['feature_names'])
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# we choose the sepal length and width
after_data_inter = total_data[total_data[:, 13] != 2, :]
after_data = after_data_inter[:, [0, 3, 13]]
# print(after_data[:5, :])

fig_index = 1
# generate model
for kernel, c, gamma in [('linear', 1.0, 'scale'), ('rbf', 1.0, 'auto')]:
    clf = SVC(kernel=kernel, C=c, gamma=gamma)
    clf.fit(after_data[:, :2], after_data[:, 2])
    predicted = clf.predict(after_data[:, :2])
    score = accuracy_score(after_data[:, 2], predicted)
    print(f'score of svc with {kernel} is {score}')

    # get the separating hyperplane
    if kernel == 'linear':
        w = clf.coef_[0]
        a = -w[0] / w[1]
        xx = np.linspace(11, 15)
        yy = a * xx - (clf.intercept_[0]) / w[1]
        margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
        yy_down = yy - np.sqrt(1 + a ** 2) * margin
        yy_up = yy + np.sqrt(1 + a ** 2) * margin

        fig = plt.figure(fig_index)
        plt.scatter(after_data[:, 0], after_data[:, 1], c=after_data[:, 2])

        plt.plot(xx, yy, 'k-')
        plt.plot(xx, yy_down, 'k--')
        plt.plot(xx, yy_up, 'k--')

        fig_index += 1


class logistic_with_kernel(object):
    def __init__(self, gamma=1.0, kernel='rbf', n_components=None):
        self.gamma = gamma
        self.classifier = LogisticRegression()
        self.n_components = n_components
        if kernel == 'rbf':
            self.kernel = RBFSampler(self.gamma, random_state=20)
        if kernel == 'nys':
            if self.n_components:
                self.kernel = Nystroem(gamma=self.gamma, random_state=10, n_components=self.n_components)
            else:
                self.kernel = Nystroem(gamma=self.gamma, random_state=10)

    def fit(self, data, target):
        data_trans = self.kernel.fit_transform(data)
        self.classifier.fit(data_trans, target)

    def predict(self, test_data):
        test_data_trans = self.kernel.fit_transform(test_data)
        return self.classifier.predict(test_data_trans)


# logistic regression with rbf kernel
# we could choose many kernels like chi square or skewed chi square

kernel_logclassifer = logistic_with_kernel(gamma=.2, kernel='nys', n_components=100)
# kernel_logclassifer = logistic_with_kernel(gamma=.2, kernel='rbf')

kernel_logclassifer.fit(after_data[:, :2], after_data[:, 2])
predicted2 = kernel_logclassifer.predict(after_data[:, :2])
kernel_logc_score = accuracy_score(after_data[:, 2], predicted2)
print('logc_with_kernel_socre is {}'.format(kernel_logc_score))

# plain logistic regression without a kernel
logc = LogisticRegression()
logc.fit(after_data[:, :2], after_data[:, 2])
predicted3 = logc.predict(after_data[:, :2])
logc_score = accuracy_score(after_data[:, 2], predicted3)
print('logc_socre is {}'.format(logc_score))
