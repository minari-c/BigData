import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.
df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:,0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:,8]

params = {
	'n_estimators': range(1, 100, 1)
    , 'learning_rate': np.arange(0.01, 0.05, 0.01)
}
'''
n_estimators : int, default=50
        The maximum number of estimators at which boosting is terminated.
        In case of perfect fit, the learning procedure is stopped early.
        Values must be in the range `[1, inf)`.

    learning_rate : float, default=1.0
        Weight applied to each classifier at each boosting iteration. A higher
        learning rate increases the contribution of each classifier. There is
        a trade-off between the `learning_rate` and `n_estimators` parameters.
        Values must be in the range `(0.0, inf)`.
'''

gs = GridSearchCV(AdaBoostClassifier(), params, n_jobs=-1)
gs.fit(X, y)
print(gs.best_params_)
print(gs.best_score_)

cscore = cross_val_score(gs,X,y,cv=5)  # 교차 검증 k=5
print('accuracy',cscore.mean())
