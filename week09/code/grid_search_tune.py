from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier


iris = load_iris()
X = iris.data[:, 2:]
y = iris.target
params = {
    # 'max_depth': range(3, 10, 1),
    # 'min_samples_split': range(2, 10, 1)
    'n_estimators': range(4, 7, 1)
    , 'min_samples_split': range(3, 7, 1)
}
gs = GridSearchCV(RandomForestClassifier(random_state=42), params, n_jobs=-1)
gs.fit(X, y)
print(gs.best_params_)
print(gs.best_score_)