from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

iris = load_iris()
X = iris.data[:, 2:]    # petal length and width
y = iris.target

df01 = DecisionTreeClassifier(max_depth=2, random_state=42)
df01.fit(X, y)

df02 = DecisionTreeClassifier(max_depth=2, random_state=42)

cscore = cross_val_score(df, X, y, cv=5)  # 교차 검증 k=5
print('accuracy', cscore.mean())
print(X.shape)