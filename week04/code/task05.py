'''
5.1) 'exam1.csv'파일을 읽고 (첫번째 행이 열이름이 되도록)
2) english의 결측치는 0으로 치환하고
3) math의 결측치는 math의 평균 값으로 치환하고
4) nclass의 결측치는 앞에 값으로 치환하고
5) print하는 code를 작성하시오
(inplace=True 사용)

'''

#과제 5
import pandas as pd

df = pd.read_csv('../csv/exam1.csv', header=0)

df['english'].fillna(0, inplace=True)
print(df)

df['math'].fillna(df['math'].mean(), inplace=True)
print(df)

df['nclass'].fillna(method='ffill', inplace=True)
print(df)




