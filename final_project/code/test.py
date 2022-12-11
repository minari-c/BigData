import pandas as pd
# conda install -c anaconda xlrd
# conda install -c anaconda openpyxl

import os
from multiprocessing import Pool, TimeoutError, freeze_support


def foo(file_name):
    print(file_name)


folder_path = '../xlsx/'

xlsx_paths = list()

file_names = os.listdir(folder_path)
for year in file_names:
    # print(os.listdir(f'{folder_path}{year}'))
    for file_name in os.listdir(f'{folder_path}{year}'):
        xlsx_paths.append(file_name)


if __name__ == '__main__':
    freeze_support()
    with Pool(processes=16) as pool:
        pool.map(foo, xlsx_paths)
        pool.close()
        pool.join()
