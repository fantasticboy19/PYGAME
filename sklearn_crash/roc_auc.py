from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, roc_curve, auc
import matplotlib.pyplot as plt

iris = load_breast_cancer()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
forest = RandomForestClassifier(random_state=22)
# print(iris.data.shape, iris.target.shape)
# (150, 4) (150,)
forest.fit(x_train, y_train)
# y_pre = forest.predict(x_test)
# accu_score = accuracy_score(y_test, y_pre)
# precision_score = precision_score(y_test, y_pre, average='macro')
# print('accu_score is {} \nprecision_score is {}'.format(accu_score,precision_score))


y_score = forest.predict_proba(x_test)
fpr, tpr, threshold = roc_curve(y_test, y_score[:, 1])

fig, axes = plt.subplots()
axes.plot(fpr, tpr)
axes.set_title('roc curve')


