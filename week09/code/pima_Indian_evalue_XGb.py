import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, cross_val_score

df = pd.read_csv('../csv/pima-indians-diabetes3.csv', header=0)

# 세부 정보를 X로 지정합니다.
X = df.iloc[:, 0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:, 8]

al = XGBClassifier()
al.fit(X, y)

c_score = cross_val_score(al, X, y, cv=5)
print(f'accuracy: {c_score.mean()}')
print(X.shape)
