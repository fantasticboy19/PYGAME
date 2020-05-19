from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import tqdm

'''
initialize the raw data from sklearn dataset

'''

bundle = load_breast_cancer()
X, y = bundle.data, bundle.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# print(X.shape, y.shape)
pca = PCA(n_components=2, random_state=123)

X_2feature_train = pca.fit_transform(X=X_train)
# print(X_2feature_train.shape)

scaler = StandardScaler()
X_scale = scaler.fit_transform(X_2feature_train)

X_test_scale = scaler.fit_transform(pca.fit_transform(X_test))

# print(X_scale[:2, :])
svc = SVC()
param = {
    'kernel': ['rbf'],
    'C': [0.1, .5, 1, 10, 30, 40, 50, 75, 100, 500, 1000],
    'gamma': [0.001, 0.005, 0.01, 0.05, 0.07, 0.1, 0.5, 1, 5, 10, 50]

}

for cv in tqdm.trange(4, 6):
    grid = GridSearchCV(svc, param_grid=param, cv=cv)
    grid.fit(X_scale, y_train)
    print(f'score for the {cv} is {grid.score(X_test_scale, y_test)}')
    print(f'best params are {grid.best_params_}')

print('training is done')