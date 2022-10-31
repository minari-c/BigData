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
sns.set_theme(style='whitegrid')
sns.countplot(data=titanic, x=titanic["class"], hue='alive', palette=['red', 'blue'], )
"""
data=None, *, x=None, y=None, hue=None, order=None, hue_order=None,
orient=None, color=None, palette=None, saturation=.75, width=.8,
dodge=True, ax=None, **kwargs
"""
plt.show()
