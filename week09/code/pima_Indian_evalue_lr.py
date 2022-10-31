import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.
df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:,0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:,8]

# params = {
# 	'n_estimators': range(1, 100, 2)
#     , 'learning_rate': np.arange(0.01, 0.05, 0.01)
# 	, 'min_child_samples': range(20, 30, 1)
# 	, 'verbose': [ -1 ]
# }

lgb = LinearRegression()
lgb.fit(X, y)
# gs = GridSearchCV(LGBMClassifier(random_state=42,), params, n_jobs=-1)
# gs.fit(X, y)
# print(gs.best_params_)
# print(gs.best_score_)

cscore = cross_val_score(lgb, X, y, cv=5)  # 교차 검증 k=5
# print('accuracy', cscore.mean())
print('rmse: ', np.mean(np.sqrt(cscore)))
