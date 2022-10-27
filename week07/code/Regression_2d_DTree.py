from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import numpy as np

np.random.seed(42)
m = 200
X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2
y = y + np.random.randn(m, 1) / 10

y = y.squeeze()
tree_reg = DecisionTreeRegressor(max_depth=3, random_state=42)
tree_reg.fit(X, y)
cscore = cross_val_score(tree_reg, X, y, cv=5, scoring='neg_mean_squared_error')
print('RMSE', np.sqrt(-cscore.mean()))

plt.figure(figsize=(10, 7))
plot_tree(tree_reg)
plt.show()
