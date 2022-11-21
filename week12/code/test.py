from IPython.display import display_html
import folium
import webbrowser as web
import os

abs_cur_path = os.getcwd()
dir_path = f'{os.path.abspath("../html/")}\\'
file_name = 'output'
file_extension = '.html'


file_count = len(os.listdir(dir_path))
#seoul_map = folium.Map(location=[37.5658,126.975146],tiles='Stamen Terrain',zoom_start=16)
#seoul_map = folium.Map(location=[37.5658,126.975146],zoom_start=16)
seoul_map = folium.Map(
	location=[37.5658,126.975146]
	, tiles='Stamen Toner'
	, zoom_start=16
	, png_enabled=True
)

output_path = f'{dir_path}{file_name}_{file_count}{file_extension}'
print(output_path)
# seoul_map.save(outfile=output_path, close_file=False)
# print(os.environ)
# for k, v in os.environ.items():
# 	print(k, v)
print(f'{output_path}')
# web.open(f'{output_path}')
# web.get('chrome').open(output_path)


# seoul_map.save(outfile='./test_map.html')

#seoul_map.save('./seoul.html')