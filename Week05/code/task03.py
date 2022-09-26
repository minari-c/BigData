# titanic 데이터에서
# 1) age 열이 25세 이상이고 남성인 행만 구하고
# 2) 이중 앞의 5행만 print하는 하는 code를 작성 하시오
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic)

# for col in titanic.columns:
# 	print(col, titanic[col].unique())

titanic.dropna(subset=['age'], inplace=True)
# print(titanic)

# 1)
result = titanic.loc[(titanic['age'] >= 25) & (titanic['sex'] == 'male'), :]
# mask 식에
# (titanic['age'] >= 25) & (titanic['sex'] == 'male') 잘됨
# titanic['age'] >= 25 & titanic['sex'] == 'male' 안 됨
# print((titanic['age'] >= 25) & (titanic['sex'] == 'male'))
# print(titanic['age'] >= 25 & titanic['sex'] == 'male')

# 2)
print(result.iloc[:5])  # [0 ~ 4]
