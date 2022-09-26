# 아래의 code에서 정의 되는 df1, df2, df3에서
# 1) df1과 df2를 위 아래로 연결하고 새로운 인덱스를 설정하여 print 히고
# 2) df1과 df3를 좌 우로 연결 하고 print하는
# code를 작성 하시오
import pandas as pd

# 데이터 프레임 1
df1 = pd.DataFrame([
        ['a', 1],
        ['b', 2]
    ],
    columns=['letter', 'number'])
# print(df1)

# 데이터 프레임 2
df2 = pd.DataFrame([
        ['c', 3],
        ['d', 4]
    ],
    columns=['letter', 'number'])
# print(df2)

# 데이터 프레임 3
df3 = pd.DataFrame([
        ['bird', 'polly'],
        ['monkey', 'george']
    ],
    columns=['animal', 'name'])
# print(df3)


# 1)
print(pd.concat([df1, df2], axis=0))


# 2)
print(pd.concat([df1, df3], axis=1))