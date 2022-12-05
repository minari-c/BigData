# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import webbrowser as web
import os
import pandas as pd
import folium

abs_cur_path = os.getcwd()
dir_path = f'{os.path.abspath("../html/")}\\'
file_name = 'output'
file_extension = '.html'
file_count = len(os.listdir(dir_path))

#  데이터프레임 변환
df = pd.read_csv('../csv/인천광역시 미추홀구_재래시장_20220822.csv',  encoding='CP949')  # 수준원점 기준

print(df)
# 지도 만들기

incheon_map = folium.Map(
	location=[37.449394, 126.657354]
	, tiles='Stamen Terrain'
	, zoom_start=14
)

# marking
for name, lat, lng in zip(df.시장명, df.위도, df.경도):
	folium.Marker([lat, lng], popup=name).add_to(incheon_map)

output_path = f'{dir_path}{file_name}_{file_count}{file_extension}'

incheon_map.save(outfile=output_path)

web.open(f'{output_path}')
web.get('chrome').open(output_path)
