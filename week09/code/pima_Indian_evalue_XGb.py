import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score

df = pd.read_csv('../csv/pima-indians-diabetes3.csv', header=0)

# 세부 정보를 X로 지정합니다.
X = df.iloc[:, 0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:, 8]

# params = {
# 	"n_estimators": range(1, 100, 2)                        # 학습 모델 수
#     , "learning_rate": np.arange(0.1, 0.3, 0.05)            # 학습률
# 	, "max_depth": range(1, 5)                              # 최대 탐색 깊이
# }

# al = XGBClassifier()
# al.fit(X, y)

xgb = XGBClassifier(learning_rate=0.15, max_depth=2, n_estimators=99)
xgb.fit(X, y)

cscore = cross_val_score(xgb, X, y, cv=5, scoring="neg_mean_squared_error")  # 교차 검증 k=5
# print('accuracy', cscore.mean())
print('rmse: ', np.mean(np.sqrt(-1 * cscore)))

# gs = GridSearchCV(XGBClassifier(random_state=42), params, n_jobs=-1)
# gs.fit(X, y)
# print(gs.best_params_)
# print(gs.best_score_)
#
# c_score = cross_val_score(gs, X, y, cv=5)
# print(f'accuracy: {c_score.mean()}')
# print(X.shape)
