import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.
df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:,0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:,8]

svc = SVC(kernel='linear')
svc.fit(X, y)

cscore = cross_val_score(svc, X, y, cv=5, scoring="neg_mean_squared_error")  # 교차 검증 k=5
# print('accuracy', cscore.mean())
print('rmse: ', np.mean(np.sqrt(-1 * cscore)))
