#과제 1
import pandas as pd

result = pd.Series(['-', 5, 6, 7, 8], index=['-', 'e', 'd', 'f', 'g'])

print(result)

#과제 2
import pandas as pd

result = pd.Series(['-', 'amy', '15', 'cse', '3'], index=['-', 0, 1, 2, 3])

print(result)

#과제 3
import pandas as pd

data = ('-', '우석', '2003-01-03', '남', 'true')

result = pd.Series(data, index=['-', '이름', '생년월일', '성별', '학교'])

# print(result)


#과제 4
import pandas as pd

data = {'e1': [1, 4, 5], 'e2': [2, 3, 3], 'e3': [3, 4, 2]}

result = pd.DataFrame(data)

# print(result)

#과제 5
import pandas as pd

result = pd.DataFrame(
    [[22, '남', '피아노'], [23, '여', '산책']],
    index=['우석', '나라'],
    columns=['나이', '성별', '취미']
)

# print(result)


#과제 6
import pandas as pd

data = pd.DataFrame(
    [[17, '고등', '피아노'], [14, '중등', '산책']],
    index=['우석', '나라'],
    columns=['나이', '학교', '취미']
)

# print(data, end='\n\n')

data.index = ['student1', 'student2']
data.columns = ['age', 'school', 'hobby']
# print(data, end='\n\n')

data.rename(index={'student1': 'data1', 'student2': 'data2'}, inplace=True)
data.rename(columns={'age': 'feat1', 'school': 'feat2', 'hobby': 'feat3'}, inplace=True)
# print(data, end='\n\n')


#과제 7
import pandas as pd
student_data = {
  '나이': [17, 14, 12, 19, 15],
  '구분': ['고등', '중등', '초등', '고등', '중등'],
  '취미': ['독서', '산책', '축구', '독서', '농구'],
  '학교': ['선경', '한국', '우성', '효성', '상성']
}
data = pd.DataFrame(student_data, index=['우석', '인아', '나라', '민정', '서준'])
# print(data, end='\n\n')

data01 = data[:]
# 1)
data01.drop('우석', inplace=True)
# print(data01, end='\n\n')

data02 = data[:]
# 2)
data02.drop(['나라', '민정'], inplace=True)
# print(data02, end='\n\n')

data03 = data[:]
# 3)
data03.drop('나이', axis=1, inplace=True)
# print(data03, end='\n\n')

data04 = data[:]
# 4)
data04.drop(['구분', '학교'], axis=1, inplace=True)
# print(data04, end='\n\n')

#과제 8
import pandas as pd
student_data = {
    '나이': [17, 14, 12, 19, 15],
    '구분': ['고등', '중등', '초등', '고등', '중등'],
    '취미': ['독서', '산책', '축구', '독서', '농구'],
    '학교': ['선경', '한국', '우성', '효성', '상성']
}
data = pd.DataFrame(student_data, index=['우석', '인아', '나라', '민정', '서준'])
# print(data.loc['우석', '구분'], end='\n\n')
#
# print('data.loc')
# print(data.loc['인아'], end='\n\n')
#
# print('data.iloc')
# print(data.iloc[1], end='\n\n')
#
# print('data.loc')
# print(data.loc[['나라', '민정']], end='\n\n')
#
# print('data.iloc')
# print(data.iloc[[2, 3]], end='\n\n')
#
# print(data[['취미', '학교']])

#과제 9
import pandas as pd
student_data = {
    '나이': [17, 14, 12, 19, 15],
    '구분': ['고등', '중등', '초등', '고등', '중등'],
    '취미': ['독서', '산책', '축구', '독서', '농구'],
    '학교': ['선경', '한국', '우성', '효성', '상성']
}
data = pd.DataFrame(student_data, index=['우석', '인아', '나라', '민정', '서준'])
# print(data, end='\n\n')
#
# print('data.loc')
# print(data.loc['인아', '취미'], end='\n\n')
#
# print('data.iloc')
# print(data.iloc[1, 2], end='\n\n')
#
# print('data.loc')
# print(data.loc['나라': '민정', '취미': '학교'], end='\n\n')
#
# print('data.iloc')
# print(data.iloc[2: 4, 2: 4], end='\n\n')


#과제 10
import pandas as pd
student_data = {
    '이름': ['우석', '인아', '나라', '민정', '서준'],
    '나이': [17, 14, 12, 19, 15],
    '구분': ['고등', '중등', '초등', '고등', '중등'],
    '취미': ['독서', '산책', '축구', '독서', '농구'],
    '학교': ['선경', '한국', '우성', '효성', '상성']
}
data = pd.DataFrame(student_data)
print(data, end='\n\n')
data.set_index('이름', inplace=True)
print(data, end='\n\n')

data['영어'] = 90
print('01', data, end='\n\n')

data.loc['영진'] = [18, '고등', '배구', '선경', 90]
print(data, end='\n\n')

data.loc['나라', ['취미', '학교']] = '농구', '선경'
print(data)


#과제 11
import pandas as pd
student_data = {
    '이름': ['우석', '인아', '나라', '민정', '서준'],
    '나이': [17, 14, 12, 19, 15],
    '구분': ['고등', '중등', '초등', '고등', '중등'],
    '취미': ['독서', '산책', '축구', '독서', '농구'],
    '학교': ['선경', '한국', '우성', '효성', '상성']
}
data = pd.DataFrame(student_data)
data.set_index('이름', inplace=True)
print(data, end='\n\n')

new_index = student_data['이름']
print(new_index)
data01 = data.reindex(new_index)
print(data01, end='\n\n')

data02 = data01.sort_index(ascending=True)
print(data02, end='\n\n')

#과제 12
import pandas as pd

data = pd.read_csv('../csv/Case.csv')
print(data, end='\n\n')

data01 = data[:]
data01.drop('city', axis=1, inplace=True)
print(data01, end='\n\n')

data01['country'] = 'korea'
print(data01, end='\n\n')

data01.to_csv('../csv/case2.csv')
