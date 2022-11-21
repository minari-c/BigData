import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

font_file_name = 'd2coding.ttc'
font_dir_path = f'{os.path.abspath("../font")}\\'
font_full_path = f'{font_dir_path}{font_file_name}'


font_prop = fm.FontProperties(fname=font_full_path, size=15)
matplotlib.rc('font', family=font_prop.get_name())
