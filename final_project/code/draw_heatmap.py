import pandas
import pandas as pd
import numpy as np
from multiprocessing import Pool, freeze_support
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

def processing_chunk(chunk):
    for row in chunk.iterrows():
        pass
    time.sleep(5)


def foo(corr_df):
	df_compt = pd.read_csv('../csv/data_compact.csv', low_memory=False)
	corr_df = df_compt.corr(method='kendall')


font_path = '../../font/d2coding.ttc'
fontprop = fm.FontProperties(fname=font_path, size=15)
plt.rc('font', family=fontprop.get_name())


# df_all = pd.DataFrame()
# csv_path_infos = list()
# for dir_name in os.listdir('../csv'):
# 	for file_name in os.listdir(f'../csv/{dir_name}'):
# 		df = pd.read_csv(f'../csv/{dir_name}/{file_name}', encoding='utf-8', low_memory=False)
# 		df_all = pd.concat([df_all, df])

# df = pd.read_csv('../csv/2022/2022년 2월.csv')


# print(df.columns)
# unique_list = list()

# print(df_all.columns)
# for colum in df_all.columns[1:]:
# 	unique_list.append(df_all[colum].unique())
# corr_df = df_compt.corr(method='pearson')
corr_df = pandas.DataFrame()
if __name__ == '__main__':  # for windows os
	freeze_support()        # for windows os
	with Pool(processes=15) as pool:
		pool_size = 15
		chunk_size = 2000 * pool_size
		count = 0
		for file_chunk in pd.read_csv('../csv/data_compact.csv', low_memory=False, chunksize=chunk_size):
			line = count * chunk_size
			print(f"Processing {chunk_size} lines after line {line}")
			
			# Split chunk evenly. It's better to use this method if every chunk takes similar time.
			pool.map(processing_chunk, pd.np.array_split(file_chunk, pool_size))
			
			count += 1
		pool.close()
		pool.join()


print(corr_df)
mask = np.triu(np.ones(corr_df.shape)).astype(np.bool)
print(mask)
ax = plt.axes()
sns.heatmap(
	corr_df
	, annot=True
	, cmap='RdYlBu_r'
	, mask=mask
	, linewidths=.5
	, cbar_kws={"shrink": .5}
	, vmin=-1
	, vmax=1
	, ax=ax
)
ax.set_title('kendall corr')

plt.show()

# corr_df = df_compt[1:].corr(method='spearman')
# corr_df = df_all[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='pearson')
# corr_df = df[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='kendall')
# corr_df = df[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='spearman')
# print(df[['측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']])


# df_compt.to_csv('../csv/data_concat.csv')
