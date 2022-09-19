'''
.code에서 정의한 데이터에서
1) 하나라도 NaN이 있는 행은 삭제하고 print하는 code  (df1에 저장 후 print)
2) 모든 값이  NaN인  행을 삭제하고 print하는 code  (df2에 저장 후 print)
3) NaN이 포함된 행을 삭제할때 데이터가 4개 이상 있어야 남기도록 하고  (df3)   print하는 code를 작성 하시오

'''

#과제 4
import pandas as pd
import numpy as np

raw_data = {
    'name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
    'age': [42, np.nan, 36, np.nan, 73],
    'math': [4, np.nan, np.nan, 2, 3],
    'physics': [25, np.nan, np.nan, 62, 70],
    'korean': [25, np.nan, np.nan, 62, 70]
}

df = pd.DataFrame(raw_data)
print(df)

df1 = df.dropna(how='any')
print(df1)

df2 = df.dropna(how='all')
print(df2)

df3 = df.dropna(thresh=4)
print(df3)

