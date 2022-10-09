'''
6.exam2.csv 파일을 읽고
1) nclass 기준으로 group별 평균을 구하고 print하고
2) nclass 기준으로 group별 최고점을 구하고 print하는 code를 작성 하시오
'''
import pandas as pd

df = pd.read_csv('../csv/exam2.csv', header=0)
# print(df)

# print(df.groupby.__doc__)
by_nclass_df = df.drop('id', axis=1).groupby('nclass')  # id 열 제거 후 nclass로 DataFrameGrouBy object 생성
# for i in by_nclass_df.__iter__():
# 	print(i)

# 1)
print(by_nclass_df.mean())

# 2)
print(by_nclass_df.max())

# https://pandas.pydata.org/docs/reference/groupby.html
