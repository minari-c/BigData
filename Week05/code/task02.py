# iris3.csv를 읽고
# 1) petal_length과 petal_width 열에 mean_min 함수를 적용하고
# 2) 결과 값을 프린트 하는 code를 작성 하시오
import pandas as pd

df = pd.read_csv('../csv/iris3.csv')


def mean_min(x):
     return x.mean() - x.min()


# 1)
result = df.loc[:, ['petal_length', 'petal_width']].apply(mean_min, axis=1)

# 2)
print(result)
