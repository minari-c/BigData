import json
import re

import matplotlib.font_manager as fm

from konlpy.tag import Okt

from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

inputFileName = '../json/code-1'
data = json.loads(open(inputFileName + '.json', 'r', encoding='utf-8').read())
print(f'data: {data}')


message = ''

for item in data:
	#    if 'message' in item.keys():
	#        message = message + re.sub(r'[^\w]', ' ', item['message']) +''
	if 'description' in item.keys():
		message = message + re.sub(r'[^\w]', ' ', item['description']) + ''


print(f'message: {message}')  # 출력하여 내용 확인


nlp = Okt()
message_N = nlp.nouns(message)
print(f'message_N: {message_N}')  # 출력하여 내용 확인

count = Counter(message_N)

print(f'count: {count}')  # 출력하여 내용 확인


word_count = dict()

for i in count.most_common(80):
	print(i)


