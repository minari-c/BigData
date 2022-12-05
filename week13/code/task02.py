from konlpy.tag import Okt
import pandas as pd
import re
import joblib
from sklearn.metrics import accuracy_score


okt = Okt()


def okt_tokenizer(text):
	tokens = okt.morphs(text)
	return tokens


test_df = pd.read_csv('../csv/test_movie_review30.csv', encoding='utf8')
print(test_df.head())
print(test_df['label'].value_counts())

test_df['review'] = test_df['review'].apply(lambda x: re.sub(r'[^ ㄱ-ㅣ가-힣]+', "", str(x)))
print(test_df['review'].head())

tfidf = joblib.load('../pkl/tf_model.pkl')
test_tfidf = tfidf.transform(test_df['review'])

lr_model = joblib.load('../pkl/lr_model.pkl')
test_predict = lr_model.predict(test_tfidf)

# test_df.dropna(inplace=True)
# test_df = test_df.reset_index()
print(test_df['label'].shape, test_predict.shape)
print(test_df['label'], test_predict, sep='\n')
'''
(31,) (31,)
0    NaN
1    NaN
2    NaN
3    NaN
4    NaN
5    NaN
6    NaN
7    NaN
8    NaN
9    NaN
10   NaN
11   NaN
12   NaN
13   NaN
14   NaN
'''
print('감성 분석 정확도: ', round(accuracy_score(test_df['label'], test_predict), 3))


print('### 영화별 긍정 review 수 ###')
print(test_df.groupby('title')['predicted_label'].sum())

mask = test_df['label'] != test_df['predicted_label']

print('### 예측이 잘못된 review')
print(test_df.loc[mask, ['review']])
test_df.to_csv('review_results.txt')
