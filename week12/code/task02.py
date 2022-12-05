import os
import webbrowser as web
import pandas as pd
import folium

df = pd.read_csv('../csv/서울특별시 성북구_약국list.csv', encoding='CP949')

abs_cur_path = os.getcwd()
dir_path = f'{os.path.abspath("../html/")}\\'
py_name = 'tesk02'
file_name = 'output'
file_extension = '.html'
file_count = len(os.listdir(dir_path))
output_path = f'{dir_path}{file_name}_{file_count}{file_extension}'

seoul_map = folium.Map(
	location=[37.61891151, 127.0552709]
	, tiles='Stamen Toner'
	, zoom_start=14
)

# marking
for name, lat, lng in zip(df.약국명, df.위도, df.경도):
	folium.Marker([lat, lng], popup=name).add_to(seoul_map)

seoul_map.save(outfile=output_path)

web.open(f'{output_path}')
web.get('chrome').open(output_path)
