import pandas as pd
import numpy as np
from multiprocessing import Pool, freeze_support
import os
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_path = '../../font/d2coding.ttc'
fontprop = fm.FontProperties(fname=font_path, size=15)
plt.rc('font', family=fontprop.get_name())

df_comp = pd.read_csv('../csv/data_compact.csv', low_memory=False)

# df_all = pd.read_csv('../csv/data_concat.csv', low_memory=False)
# df_reduce = df_all[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']]
#
# print(df_reduce)
# df_reduce.to_csv('../csv/data_compact.csv')
