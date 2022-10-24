'''
6.아래 code에서 정의하는 데이터 프레임에서
1) 중복 행을 제거 하고 print하는 code(df1)
2) c1,c3을 기준으로 중복행을 제거 하고 print하는 code(df2)
를 작성 하시오.
'''

#과제 6
import pandas as pd

df = pd.DataFrame({
    'c1': ['a', 'a', 'b', 'a', 'b'],
    'c2': [2, 1, 2, 1, 2],
    'c3': [1, 1, 2, 2, 2]
})
df1 = df.duplicated()
print(df1)

df2 = df[['c1', 'c3']].drop_duplicates()
print(df2)
