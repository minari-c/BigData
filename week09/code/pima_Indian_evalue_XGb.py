import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.
df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:,0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:,8]

params = {
	'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
}
'''
{'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}
'''

gs = GridSearchCV(SVR(), params, n_jobs=-1)
gs.fit(X, y)
print(gs.best_params_)
print(gs.best_score_)

cscore = cross_val_score(gs, X, y, cv=5)  # 교차 검증 k=5
print('accuracy: ',cscore.mean())



