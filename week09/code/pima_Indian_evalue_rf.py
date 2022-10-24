import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from matplotlib import pyplot

# 피마 인디언 당뇨병 데이터셋을 불러옵니다.
df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:,0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:,8]

al = RandomForestClassifier(n_estimators=10)
al.fit(X, y)

cscore=cross_val_score(al,X,y,cv=5)  # 교차 검증 k=5
print('accuracy',cscore.mean())
print(X.shape)
