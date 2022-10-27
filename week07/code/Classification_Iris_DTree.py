from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()
X = iris.data[:, 2:]    # petal length and width
y = iris.target

df = DecisionTreeClassifier(max_depth=3, random_state=42)
df.fit(X, y)

cscore = cross_val_score(df, X, y, cv=5)
print('accuracy: ', cscore.mean())
print(X.shape)

plt.figure(figsize=(10, 7))
plot_tree(df)
plt.show()
