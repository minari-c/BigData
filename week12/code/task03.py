import os
import webbrowser as web
import pandas as pd
import folium

df = pd.read_csv('../csv/seoul_population.csv', encoding='utf-8')

seoul_geo = '../json/서울행정구역경계.json'

abs_cur_path = os.getcwd()
dir_path = f'{os.path.abspath("../html/")}\\'
py_name = 'task03'
file_name = 'output'
file_extension = '.html'
file_count = len(os.listdir(dir_path))
output_path = f'{dir_path}{file_name}_{file_count}{file_extension}'

seoul_map = folium.Map(
	location=[37.56891151, 127.0052709]
	, tiles='Stamen Toner'
	, zoom_start=10
)

folium.Choropleth(
	geo_data=seoul_geo
	, data=df
	, columns=['시군구명', '인구수']
	, fill_color='YlOrRd'
	, fill_opacity=0.7
	, line_opacity=0.3
	, threshold_scale=[100, 150, 250, 400, 500, 800]
	, key_on='feature.properties.name'
).add_to(seoul_map)

seoul_map.save(outfile=output_path)

web.open(f'{output_path}')

