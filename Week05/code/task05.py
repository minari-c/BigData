#
# 5.아래의 code에서 정의 되는 adf, bdf에서
# 1) x1 열을 기준으로 adf, bdf의 교집합을 병합하고 print
# 2) x1 열을 기준으로 adf, bdf의 합집합을 병합하고 print
# 3) x1 열을 기준으로 왼쪽 데이터 프레임(adf)을 기준으로 병합하고 print
# 4) x1 열을 기준으로 오른쪽 데이터 프레임(bdf)을 기준으로 병합하고 print
# 하는 code를 작성하시오

import pandas as pd

# 실습을 위한 데이터 프레임 만들기 1
adf = pd.DataFrame({
    "x1": ["A", "B", "C"],
    "x2": [1, 2, 3]
})
print(adf)
# 데이터 프레임 만들기 2
bdf = pd.DataFrame({
    "x1": ["A", "B", "D"],
    "x3": ["T", "F", "T"]
})
print(bdf)

# print(pd.merge.__doc__)
# 1)
print(pd.merge(left=adf, right=bdf, how='inner', on='x1'), end='\n\n')

# 2)
print(pd.merge(left=adf, right=bdf, how='outer', on='x1'), end='\n\n')

# 3)
print(pd.merge(left=adf, right=bdf, how='left', on='x1'), end='\n\n')

# 4)
print(pd.merge(left=adf, right=bdf, how='right', on='x1'), end='\n\n')
