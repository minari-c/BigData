import pandas as pd

df_mpg = pd.read_csv('../csv/mpg.csv',  header=0)
df_fuel = pd.read_csv('../csv/fuel.csv', header=0)

merge_df = pd.merge(left=df_mpg, right=df_fuel, how='left', on='fl')
print(merge_df.groupby(by='fl')['displ'].sum())


