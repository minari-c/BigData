import pandas as pd

df = pd.read_csv('../csv/PatientInfos.csv', header=0)

print(df.duplicated().sum())
print(df.drop_duplicates())



