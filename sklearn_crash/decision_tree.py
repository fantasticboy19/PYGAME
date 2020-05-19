from sklearn.datasets import load_wine, load_boston
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn_crash.graph_visualization import graph_generator
from sklearn.model_selection import cross_validate, cross_val_score

# use the gini index to build a decision_tree
def tree_classifier():
    tree_model = DecisionTreeClassifier(criterion='gini', random_state=20)
    wine = load_wine()
    # print(len(wine.target))
    print(dict(wine).keys())
    # print(wine.feature_names)
    feature_names = wine.feature_names
    target_names = wine.target_names
    wine_train, wine_test, wine_train_target, wine_test_target = train_test_split(wine.data, wine.target, test_size=0.3)

    tree_model.fit(wine_train, wine_train_target)
    benchmark = tree_model.score(wine_test, wine_test_target)

    print('socre is ', benchmark)

    graph_generator(decision_tree=tree_model, feature_names=feature_names, target_names=target_names, graph_name='tree')


# use the girdsearchcv to find the best params fitting to the model
def tree_regression():
    tree_model = DecisionTreeRegressor()
    boston = load_boston()
    boston_train, boston_test, boston_train_target, boston_test_target = train_test_split(boston.data, boston.target, test_size=0.3)
    para_grid = {'max_depth': list(range(5)),
                 'min_samples_split': list(range(2, 6)),
                 'min_samples_leaf': list(range(1, 6)), }
    grid_tree = GridSearchCV(tree_model, param_grid=para_grid, n_jobs=-1, verbose=2, cv=10)
    grid_tree.fit(boston_train, boston_train_target)

    best_tree = grid_tree.best_estimator_
    return best_tree.score(boston_test, boston_test_target), grid_tree.best_params_

# use the cross_validate or cross_val_score
def tree_regression2():
    tree_model = DecisionTreeRegressor(random_state=20)
    boston = load_boston()
    # boston_train, boston_test, boston_train_target, boston_test_target = train_test_split(boston.data, boston.target, test_size=0.3)
    train, label = boston.data, boston.target
    # para_grid = {'max_depth': list(range(5)),
    #              'min_samples_split': list(range(2, 6)),
    #              'min_samples_leaf': list(range(1, 6)), }
    # grid_tree = GridSearchCV(tree_model, param_grid=para_grid, n_jobs=-1, verbose=2, cv=10)
    # grid_tree.fit(boston_train, boston_train_target)
    #
    # best_tree = grid_tree.best_estimator_
    # return best_tree.score(boston_test, boston_test_target), grid_tree.best_params_
    cv_result = cross_validate(tree_model, train, label, cv=10)
    return cv_result


if __name__ == '__main__':
    # score, params = tree_regression()
    # print(f'score is {score}, and the best params are {params}')
    cv_result = tree_regression2()
    print(cv_result.keys())
    print(cv_result['test_score'].mean())
