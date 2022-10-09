'''
4.exam_s.csv 파일을 열고
데이터 프레임의 요약 정보를 print하고
math 열의 데이터 type이 int가 될 수 있도록 int가 아닌 데이터가 들어 있는 행을 삭제하고
math열의 데이터 형을 int로 변경하고
요약 정보를 다시 print하는 code를 작성 하시오.
'''
import numpy as np
import pandas as pd

df = pd.read_csv('../csv/exam_s.csv', header=0)
# 01
# print(df.info(), end='\n\n')

# 02
def isndigit(x: str) -> bool:
	return not x.isdigit()

df.mask(df['math'].apply(lambda x: isndigit(x)), inplace=True)  # change float64
df.dropna(inplace=True)

# 03
df['math'] = df['math'].astype('int64')
# or df = df.astype('int64')

# 04
print(df.info())


