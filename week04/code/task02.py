#과제 2
import pandas as pd

student_data = {
    '이름': ['우석', '인아', '나라', '민정'],
    '국어': [90, 80, 75, 90],
    '영어': [85, 90, 85, 95],
    '물리': [70, 80, 80, 90],
    '화학': [50, 70, 90, 100]
}
df = pd.DataFrame(student_data)

df.set_index('이름', inplace=True)

df['인문'] = df[['영어', '국어']].sum(axis=1).values

df['과학'] = df[['물리', '화학']].sum(axis=1).values

df.sort_values(by='과학', ascending=0, inplace=True)

print(df)
