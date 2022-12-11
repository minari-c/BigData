import pandas as pd
# conda install -c anaconda xlrd
# conda install -c anaconda openpyxl

import os
from multiprocessing import Pool, TimeoutError, freeze_support


def foo(file_info):
    xlsx = pd.read_excel(f'{file_info[0]}{file_info[1]}{file_info[2]}.xlsx')
    xlsx.to_csv(f'../csv/{file_info[1]}{file_info[2]}.csv')


folder_path = '../xlsx/'
xlsx_path_infos = list()


file_names = os.listdir(folder_path)
for year in file_names:
    # print(os.listdir(f'{folder_path}{year}'))
    for file_name in os.listdir(f'{folder_path}{year}'):
        xlsx_path_infos.append([folder_path, f'{year}/', file_name[:file_name.find('.')]])


if __name__ == '__main__':  # for windows os
    freeze_support()        # for windows os
    for year in file_names:
        os.mkdir(f'../csv/{year}')
    with Pool(processes=15) as pool:
        pool.map(foo, xlsx_path_infos)
        pool.close()
        pool.join()
