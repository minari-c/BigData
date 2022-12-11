import pandas as pd
# conda install -c anaconda xlrd
# conda install -c anaconda openpyxl

import os
from multiprocessing import Pool, TimeoutError, freeze_support


def foo(file_info):
    print(file_info)


folder_path = '../xlsx/'
xlsx_path_infos = list()


file_names = os.listdir(folder_path)
for year in file_names:
    # print(os.listdir(f'{folder_path}{year}'))
    for file_name in os.listdir(f'{folder_path}{year}'):
        xlsx_path_infos.append([f'{folder_path}{year}/', file_name])


if __name__ == '__main__':  # for windows os
    freeze_support()        # for windows os
    with Pool(processes=16) as pool:
        pool.map(foo, xlsx_path_infos)
        pool.close()
        pool.join()
