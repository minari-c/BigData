import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, VotingClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

df = pd.read_csv('../csv/pima-indians-diabetes3.csv')

X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

clf1 = AdaBoostClassifier()
clf2 = SVC()
clf3 = XGBClassifier()
clf4 = LGBMClassifier()

classifier = VotingClassifier(
	estimators=[ ('ada', clf1), ('svc', clf2), ('xgb', clf3), ('lgbm', clf4) ]
	, verbose=True
)
classifier.fit(X,y)

cscore = cross_val_score(classifier, X, y, cv=5)  # 교차 검증 k=5
print('accuracy: ', cscore.mean())