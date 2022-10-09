import numpy as np
import pandas as pd

df = pd.read_csv('../csv/exam.csv')

# 1)
df_group = df.groupby(by=['nclass', 'year'])
print(df_group.mean().iloc[1:])
# FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
#   print(df_group['math', 'english', 'science'].mean())

# 2)
def is_pass(math, thresh):
	result = 'pass'
	if math < thresh:
		result = 'fail'
	else:
		result = 'pass'
	return result


df['math_pass'] = df.apply(lambda x: is_pass(x['math'], 80), axis=1)
print(df['math_pass'])
df['eng_pass'] = df.apply(lambda x: is_pass(x['english'], 90), axis=1)
print(df['eng_pass'])

print(df.groupby(by=['math_pass', 'eng_pass'])['science'].mean())


'''
3.‘exam.csv’ 파일을 읽고
nclass와 year 을 기준으로 group을 나누고 group 별 ‘math’,‘english’,‘science’ 평균을 출력하고
‘math_pass’ 라는 열을 추가 하고 math 점수가 80이상이면 ‘pass’ 아니면 ‘fail’ 이라고 저장하고
‘eng_pass’ 라는 열을 추가 하고 english 점수가 90이상이면 ‘pass’ 아니면 ‘fail’ 이라고 저장하고
‘math_pass’,’eng_pass’를 기준으로 group을 나눈 후 group별 science 평균을 print하는 code를 작성하시오
'''