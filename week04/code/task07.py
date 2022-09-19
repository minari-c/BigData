
'''
7.1) wine1.csv 파일을 읽고 (첫행부터 데이터로 읽음)
2) column 이름을 'country', 'year','feat1','fest2','fest3','feat4'로 지정하고
3) country의 누락 데이터는 france로 저장하고
4) feat1, feat2, feat3, feat4의 누락 데이터는 각 열의 평균으로 저장하고
5) 'country','year' 기준으로 중복데이터를 제거 하고
6) 'feat1-2' 열을 추가 하여 feat1과 feat2의 핪의 값을 저장하고
7) 'year'를 기준으로 오름 차순으로 출력하는 code를 작성 하시오.
'''

#과제 7
import pandas as pd

df = pd.read_csv('../csv/wine1.csv', header=0)

df.columns = ['country', 'year', 'feat1', 'fest2', 'fest3', 'feat4']

df['country'].fillna('france', inplace=True)


name = ['feat1', 'fest2', 'fest3', 'feat4']

fill_val = dict()
for n in name:
	fill_val[n] = df[n].mean()

print(fill_val)

df[['feat1', 'fest2', 'fest3', 'feat4']].fillna(fill_val, inplace=True)
print(df)
