import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier

df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

# 세부 정보를 X로 지정합니다.
X = df.iloc[:, 0:8]
# 당뇨병 여부를 Y로 지정합니다.
y = df.iloc[:, 8]

ada = AdaBoostClassifier(n_estimators=1000)

# 앞 예제에서 만들어진 X_data, y_target 데이터 셋을 적용하여 학습합니다.
ada.fit(X, y)

feature_series = pd.Series(data=ada.feature_importances_, index=X.columns )
#feature_series = feature_series.sort_values(ascending=False)
sns.barplot(x= feature_series, y=feature_series.index)
plt.show()
