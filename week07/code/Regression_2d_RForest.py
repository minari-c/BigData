import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

np.random.seed(42)
m = 200
X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2
y = y + np.random.randn(m, 1) / 10

y = y.squeeze()
tree_reg = RandomForestRegressor(n_estimators=50)
tree_reg.fit(X, y)
cscore = cross_val_score(tree_reg, X, y, cv=5, scoring='neg_mean_squared_error')
print('RMSE', np.sqrt(-cscore.mean()))
print(X.shape)
print(y.shape)
