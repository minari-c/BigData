'''
3.1) iris3.csv 파일을 읽고 (첫번째 행을 column 이름으로)
2) column 이름을 'feat1','feat2','feat3','feat4','name'으로 변경하고
3) 처음 3개 행을 print하고
4) 요약 정보를 print하고
5) 통계 정보를 print하고
6) 각 열 데이터의 고유값 개수를 print하고
7) 'feat2' 열의 최대값 print
8) 'feat4' 열의 표준 편차 print
9) 'feat1'과 'feat3'의 상관계수를 출력하는 코드를 작성 하시오.
'''
#과제 3
import pandas as pd

df = pd.read_csv('../csv/iris3.csv', header=0)

# 01
# print(df.head)

# 02
df.columns = ['feat1', 'feat2', 'feat3', 'feat4', 'name']
print(df)

# 03
print(df.head(3))

# 04
print(df.info())

# 05
print(df.describe())

# 06
print(df[:].value_counts())

# 07
print(df['feat2'].max())

# 08
print(df['feat4'].std())

# 09
print(df[['feat1', 'feat3']].corr())