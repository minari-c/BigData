#과제 1
import pandas as pd

student_data = {
    '이름': ['우석', '인아', '나라', '민정', '서준'],
    '나이': [17, 14, 12, 19, 15],
    '구분': ['고등', '중등', '초등', '고등', '중등'],
    '취미': ['독서', '산책', '축구', '독서', '농구'],
    '학교': ['선경', '한국', '우성', '효성', '상성']
}
df = pd.DataFrame(student_data)

# 01
df.set_index('이름', inplace=True)

# 02
df.drop('취미', axis=1, inplace=True)

# 03
df.drop('나라', axis=0, inplace=True)

# 04
df.loc['지민'] = [16, '중등', '효성']

# 05
df.rename(index={'학교': '교명'})

# 06
df.loc[['우석', '인아'], '학교'] = ['선경1', '한국1']

# 07
df.sort_values(by='나이', ascending=1, inplace=True)

# 08
df['국적'] = '한국'

print(df)
