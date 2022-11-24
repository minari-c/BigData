# 4. '결혼 유무'를 기준으로 빈도(countplot)를 나타내는 그래프를 작성하시오.
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import init_kor_font

warnings.simplefilter(action='ignore', category=FutureWarning)

filename = '../csv/welfareClean.csv'
df = pd.read_csv(filename, encoding='cp949')

print(df['결혼 유무'])
sns.countplot(
	data=df
	, x=df['결혼 유무']
	, palette=['gray', 'red', 'blue']
)

plt.show()
