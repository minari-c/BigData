# 6.exam2.csv 파일을 읽고
# 1) nclass 기준으로 group별 평균을 구하고 print하고
# 2) nclass 기준으로 group별 최고점을 구하고 print하는
# code를 작성 하시오

import pandas as pd

df = pd.read_csv('../csv/exam2.csv', header=0)
print(df)

# print(df.groupby.__doc__)
# 1)

print(df.groupby('nclass').mean())

# 2)
print(df.groupby('nclass').max())
