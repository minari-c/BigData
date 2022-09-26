'''
iris3.csv를 읽고
1) species 열의 고유값을 프린트 하고
2) sepal_length 열의 값을 첫번째 방법으로 정규화 하고
	-> new_value=value/max
3) sepal_width 열의 값을 두번째 방법으로 정규화하고
	-> new_value=(value-min)/(max-min)
4) sepal_length 열과 sepal_width 열의 통계 정보를 print하는 code를 작성 하시오.
'''
import pandas as pd

df = pd.read_csv('../csv/iris3.csv')
print(df)
print(df.columns)

# 1)
print(df['species'].unique())

# 2)
df['sepal_length'] = df['sepal_length'] / df['sepal_length'].max()
print(df['sepal_length'])

# 3)
df['sepal_width'] = \
	(df['sepal_width'] - df['sepal_width'].min()) / (df['sepal_width'].max() - df['sepal_width'].min())
# print(df['sepal_width'])

# 4)
for col_name in ['sepal_length', 'sepal_width']:
	print(df[col_name].describe())



# print(df.nunique(axis=0))
#
# for col in df.head(0):
# 	print(col, df[col].unique(), sep='\n', end='\n\n')



