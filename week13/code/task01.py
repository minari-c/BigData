import json
import os

import n_news_api as n_api


out_folder_dir = f'{os.path.abspath("../json")}\\'
out_file_name = f'task-{len(os.listdir(out_folder_dir))}.json'
full_dir = f'{out_folder_dir}{out_file_name}'

print(out_folder_dir)

node = 'news'  # 크롤링 할 대상
srcText = input('검색어를 입력하세요: ')
cnt = 0
jsonResult = []

jsonResponse = n_api.getNaverSearch(node, srcText, 1, 100)
total = jsonResponse['total']

while (jsonResponse is not None) and (jsonResponse['display'] != 0):
	for post in jsonResponse['items']:
		cnt += 1
		n_api.getPostData(post, jsonResult, cnt)

	start = jsonResponse['start'] + jsonResponse['display']
	jsonResponse = n_api.getNaverSearch(node, srcText, start, 100)

print(f'전체 검색: {total} 건')

with open(f'{full_dir}', 'w', encoding='utf8') as outfile:
	jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

	outfile.write(jsonFile)

print(f'가져온 데이터: {cnt} 건')
print(f'{out_file_name} SAVED')




"""
과제) 네이버 뉴스에서 본인이 선택한 검색어로 검색 한 결과를 json으로 저장 한 후
1) 적절하지 않은 단어를 제거 한 후
2) 단어 빈도수 기준으로 histogram 생성
3) word cloud 생성.

아래 code를 변형 하여 사용.
가능 하면 본인의 client id와 client secret 사용 할 것. 2주차 과제에 업로드 된 code확인
"""