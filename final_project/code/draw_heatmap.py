﻿import pandas as pd
import numpy as np
from multiprocessing import Pool, freeze_support
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


font_path = '../../font/d2coding.ttc'
fontprop = fm.FontProperties(fname=font_path, size=15)
plt.rc('font', family=fontprop.get_name())

df = pd.read_csv('../csv/2022/2022년 1월.csv')
print(df.columns)
unique_list = list()

print(df.columns)
for colum in df.columns[1:]:
	# print(df[colum].unique())
	# print(colum, len(df[colum].unique()))
	unique_list.append(df[colum].unique())
# print(df['지역'].unique())
'''
['서울 중구' '서울 용산구' '서울 종로구' '서울 광진구' '서울 성동구' '서울 중랑구' '서울 동대문구' '서울 성북구'
 '서울 도봉구' '서울 은평구' '서울 서대문구' '서울 마포구' '서울 강서구' '서울 구로구' '서울 영등포구' '서울 동작구'
 '서울 관악구' '서울 강남구' '서울 서초구' '서울 송파구' '서울 강동구' '서울 금천구' '서울 강북구' '서울 양천구'
 '서울 노원구' '경기 수원시' '경기 성남시' '경기 의정부시' '경기 안양시' '경기 광명시' '경기 안산시' '경기 과천시'
 '경기 구리시' '경기 의왕시' '경기 시흥시' '경기 남양주시' '경기 평택시' '경기 파주시' '경기 고양시' '경기 광주시'
 '경기 용인시' '경기 이천시' '경기 포천시' '경기 김포시' '경기 군포시' '경기 오산시' '경기 하남시' '경기 화성시'
 '경기 양주시' '경기 동두천시' '경기 안성시' '경기 여주시' '경기 연천군' '경기 가평군' '경기 양평군' '강원 춘천시'
 '강원 양구군' '강원 동해시' '강원 철원군' '강원 화천군' '강원 인제군' '강원 고성군' '부산 중구' '부산 동구'
 '부산 영도구' '부산 부산진구' '부산 동래구' '부산 남구' '부산 사상구' '부산 북구' '부산 금정구' '부산 해운대구'
 '부산 사하구' '부산 강서구' '부산 연제구' '부산 기장군' '부산 수영구' '부산 서구' '경남 창원시' '울산 동구'
 '울산 중구' '울산 남구' '울산 울주군' '울산 북구' '경남 진주시' '경남 하동군' '경남 김해시' '경남 거제시'
 '경남 사천시' '경남 양산시' '경남 밀양시' '경남 통영시' '경남 고성군' '경남 거창군' '경남 함안군' '경남 함양군'
 '경남 남해군' '경남 산청군' '경남 의령군' '경남 창녕군' '경남 합천군' '광주 동구' '광주 서구' '광주 남구'
 '광주 북구' '광주 광산구' '전북 전주시' '전남 목포시' '전남 여수시' '전남 순천시' '전남 나주시' '전남 담양군'
 '전남 장성군' '전남 광양시' '전남 해남군' '전남 영암군' '전남 화순군' '전남 영광군' '전남 장흥군' '전남 진도군'
 '전남 완도군' '전남 함평군' '전남 고흥군' '전남 신안군' '전남 무안군' '전남 강진군' '전남 곡성군' '전남 구례군'
 '전남 보성군' '제주 제주시' '제주 서귀포시' '대구 중구' '대구 수성구' '대구 동구' '대구 서구' '대구 남구'
 '대구 북구' '대구 달서구' '대구 달성군' '경북 포항시' '경북 경주시' '경북 김천시' '경북 안동시' '경북 구미시'
 '경북 영주시' '경북 경산시' '경북 상주시' '경북 칠곡군' '경북 영덕군' '경북 문경시' '경북 성주군' '경북 영천시'
 '경북 의성군' '경북 울진군' '경북 봉화군' '경북 울릉군' '경북 고령군' '경북 군위군' '경북 영양군' '경북 예천군'
 '경북 청도군' '대전 대덕구' '대전 중구' '대전 유성구' '대전 동구' '대전 서구' '충북 청주시' '충남 천안시'
 '충남 공주시' '충남 부여군' '충남 서산시' '충남 당진시' '충남 아산시' '충남 논산시' '충남 태안군' '충남 예산군'
 '충남 보령시' '충남 홍성군' '충남 금산군' '충남 청양군' '충남 계룡시' '충남 서천군' '세종 세종시' '강원 원주시'
 '강원 강릉시' '강원 삼척시' '강원 평창군' '강원 정선군' '강원 횡성군' '강원 양양군' '강원 속초시' '강원 홍천군'
 '강원 영월군' '강원 태백시' '충북 충주시' '충북 제천시' '충북 단양군' '충북 괴산군' '충북 진천군' '충북 음성군'
 '충북 영동군' '충북 증평군' '충북 보은군' '충북 옥천군' '전북 군산시' '전북 익산시' '전북 정읍시' '전북 남원시'
 '전북 고창군' '전북 부안군' '전북 김제시' '전북 완주군' '전북 진안군' '전북 임실군' '전북 무주군' '전북 순창군'
 '전북 장수군' '경북 청송군' '인천 중구' '인천 동구' '인천 남동구' '인천 미추홀구' '인천 부평구' '인천 서구'
 '인천 계양구' '인천 강화군' '인천 연수구' '경기 부천시' '인천 옹진군']
'''
corr_df = df[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='pearson')
# corr_df = df[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='kendall')
# corr_df = df[['측정소코드', '측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']].corr(method='spearman')
# print(df[['측정일시', 'SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']])
print(corr_df)
mask = np.triu(np.ones(corr_df.shape)).astype(np.bool)
print(mask)
# print(df[df.columns[1:]])
# print(df[df.columns[1:]].corr(method='pearson'))
ax = plt.axes()
sns.heatmap(
	corr_df
	, annot=True
	, cmap='RdYlBu_r'
	, mask=mask
	, linewidths=.5
	, cbar_kws={"shrink": .5}
	, vmin=-1
	, vmax=1
	, ax=ax
)
ax.set_title('pearson corr')

# sns.set_theme(style='whitegrid')
# sns.countplot(data=df, x=df['CO'], palette='Set2')
plt.show()

# if __name__ == '__main__':  # for windows os
#     freeze_support()        # for windows os
#     with Pool(processes=15) as pool:
#         pool.map(foo, xlsx_path_infos)
#         pool.close()
#         pool.join()
