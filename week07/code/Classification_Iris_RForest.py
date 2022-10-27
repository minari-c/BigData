from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data[:, 2:]
y = iris.target

df = RandomForestClassifier(n_estimators=30)
df.fit(X, y)

cscore = cross_val_score(df, X, y, cv=5)
print('accuracy', cscore.mean())
print(y.shape)
