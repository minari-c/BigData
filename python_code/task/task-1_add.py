# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json

client_id = 'EjbHjpgKv0gwN1C05qn6'
client_secret = 'FDtN2OazP7'

encText = urllib.parse.quote('태풍')
url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText     # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.read().decode('utf-8')

if rescode == 200:
	response_body = response.read()
	print(response_body.decode('utf-8'))
else:
	print("Error Code:" + rescode)

jsonResult = json.loads(rescode)

with open('../json/task-1_add.json', 'w', encoding='utf8') as outfile:
	jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
	
	outfile.write(jsonFile)