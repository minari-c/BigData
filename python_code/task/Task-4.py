import json
import re

import matplotlib.font_manager as fm

from konlpy.tag import Okt

from collections import Counter

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from wordcloud import WordCloud

inputFileName = '../json/task-1'
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

for tag, counts in count.most_common(80)[2:-1]:
	if len(str(tag)) > 1:
		word_count[tag] = counts
		print("%s : %d" % (tag, counts))

font_path = '../font/d2coding.ttc'
fontprop = fm.FontProperties(fname=font_path, size=15)
# matplotlib.rc('font', family=font_name)
# fm._rebuild()

plt.rc('font', family=fontprop.get_name())

plt.figure(figsize=(12, 5))
plt.xlabel('키워드')
plt.ylabel('빈도수')
plt.grid(True)

sorted_Keys = sorted(word_count, key=word_count.get, reverse=True)
sorted_Values = sorted(word_count.values(), reverse=True)

plt.bar(range(len(word_count)), sorted_Values, align='center')
plt.xticks(range(len(word_count)), list(sorted_Keys), rotation='90')

plt.show()

wc = WordCloud(font_path, background_color='ivory', width=800, height=600)
cloud = wc.generate_from_frequencies(word_count)

plt.figure(figsize=(8, 8))
plt.imshow(cloud)
plt.axis('off')
plt.show()

cloud.to_file('Task-04.jpg')

