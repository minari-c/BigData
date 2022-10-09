'''
(선택) 7. stock price 파일과 stock valuation 파일을 이용하는 문제입니다
1) id를 중심으로 병합된 데이터프레임(adf)를 만들어주세요, (교집합)

2) adf 데이터프레임을 이용해
	시가총액(value)이 10000 이상인 기업들의 주가(price), 주가수익비율(per), 주가자산비율(pbr)의 표준편차를 구하세요

3-1) 기존의 per열은 삭제한 후 새롭게 per_new열을 price와 eps를 사용해 추가해주세요
	adf 데이터프레임을 사용합니다.
	주가수익비율(per)은 주가(price)에서 주당순이익(eps)을 나눠서 계산합니다.
	예시) per = price / eps

3-2) per_new값이 15 이상인 기업은 고평가 15미만인 기업은 저평가를 나타내주는 per_value 열을 만들어주세요
	(단, lambda와 apply를 사용해주세요)

4) adf를 프린트 합니다
'''

import numpy as np
import pandas as pd

df_price = pd.read_excel('../xlsx/stock price.xlsx', header=0, engine='openpyxl')
# ExcelFile class를 생성할 때 path_or_buffer parmeter를 통해
# xls, xlsb 등의 포멧을 인식해서 engine을 알아서 선택해준다. -> path에 파일 형식이 있으면 engine parm은 쓰지 않아도 된다.
'''
path_or_buffer : str, bytes, path object (pathlib.Path or py._path.local.LocalPath),
        a file-like object, xlrd workbook or openpyxl workbook.
        If a string or path object, expected to be a path to a
        .xls, .xlsx, .xlsb, .xlsm, .odf, .ods, or .odt file.
# First argument can also be bytes, so create a buffer
        if isinstance(path_or_buffer, bytes):
            path_or_buffer = BytesIO(path_or_buffer)

        # Could be a str, ExcelFile, Book, etc.
        self.io = path_or_buffer
'''
df_value = pd.read_excel('../xlsx/stock valuation.xlsx', header=0, engine='openpyxl')

# print(df_price['stock_name'].unique())
# print(df_value['name'].unique())

# 1)
adf = pd.merge(df_price, df_value, how='inner', on='id')
# print(adf.head(0), end='\n\n')    # Columns: [id, stock_name, value, price, name, eps, bps, per, pbr]

# 2) 시가총액(value)이 10000 이상인 기업들의 주가(price), 주가수익비율(per), 주가자산비율(pbr)의 표준편차를 구하세요
# print(type((adf['value'] >= 10000)))  # <class 'pandas.core.series.Series'>
print(adf.loc[(adf['value'] >= 10000), ['price', 'per', 'pbr']].std())


# 3-1) 기존의 per열은 삭제한 후 새롭게 per_new열을 price와 eps를 사용해 추가해주세요
adf.drop(['per'], axis=1, inplace=True)
adf['per_new'] = adf.apply(lambda x: x['price'] / x['eps'], axis=1)
# print(adf.loc[:, ['price', 'eps']])
# print(adf.loc[:, ['price', 'eps']].values.tolist())
# adf['per_new'] = [x[0] / x[1] for x in adf.loc[:, ['price', 'eps']].values]
# 'new_per' -> 'per_new'...

# 3-2) per_new값이 15 이상인 기업은 고평가 15미만인 기업은 저평가를 나타내주는 per_value 열을 만들어주세요
# 	(단, lambda와 apply를 사용해주세요)
adf['per_value'] = adf.apply(lambda x: '고평가' if x['per_new'] >= 15 else '저평가', axis=1, result_type='expand')
# print(adf['per_value'])

# 4)
print(adf)
