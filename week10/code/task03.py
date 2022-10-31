import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
df = pd.DataFrame(titanic)
print(df.head())
"""
   survived  pclass     sex   age  ...  deck  embark_town  alive  alone
0         0       3    male  22.0  ...   NaN  Southampton     no  False
1         1       1  female  38.0  ...     C    Cherbourg    yes  False
2         1       3  female  26.0  ...   NaN  Southampton    yes   True
3         1       1  female  35.0  ...     C  Southampton    yes  False
4         0       3    male  35.0  ...   NaN  Southampton     no   True
"""
# print(titanic['class'].value_counts())
size = titanic['class'].count()
# print(list(titanic['class'].value_counts() / size))
print(list(titanic['class'].value_counts() / size)[0])

labels = titanic['class'].unique()
colors = ['red', 'blue', 'green']
wedgeprops = dict(edgecolor='k', linestyle='-', linewidth=2)
textprops = dict(rotation=0, size=15, weight='bold', color='black', )

pie = plt.pie(
	x=titanic['class'].value_counts()
	, explode=[(list(titanic['class'].value_counts() / size)[0]) * 0.2, 0.05, 0.05]
	, labels=labels
	, colors=colors
	, autopct='%.1f%%'
	, startangle=180
	, wedgeprops=wedgeprops
	, shadow=True
	, textprops=textprops
	, rotatelabels=True
	, data=titanic
)
"""
x, explode=None, labels=None, colors=None, autopct=None,
pctdistance=0.6, shadow=False, labeldistance=1.1,
startangle=0, radius=1, counterclock=True, wedgeprops=None,
textprops=None, center=(0, 0), frame=False,
rotatelabels=False, *, normalize=True, data=None
"""
plt.legend(
	pie[0]
	, labels
	, loc='best'
	, frameon=True
	# , ncol=3
	, shadow=True
)
plt.show()
