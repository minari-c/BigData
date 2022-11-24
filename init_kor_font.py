import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_file_name = 'd2coding.ttc'
font_dir_path = f'C:\\pycharm_project\\BigData\\font'
font_full_path = f'{font_dir_path}\\{font_file_name}'

# 마이너스 표시 문제 해결
mpl.rcParams['axes.unicode_minus'] = False

font_prop = fm.FontProperties(fname=font_full_path, size=15)
mpl.rc('font', family=font_prop.get_name())
