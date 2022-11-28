import FinanceDataReader as fdr
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# tensorflow.python.
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import LSTM
from tensorflow.python.keras.layers import SimpleRNN
import tensorflow.python.keras.losses as losses

import matplotlib.pyplot as plt


def make_sample(data, window):  # window => 한번에 기억하는 텀
	train = list()
	target = list()
	
	for i in range(len(data) - window):
		train.append(data[i: i + window])
		target.append(data[i + window])
	return np.array(train), np.array(target)


kakao = fdr.DataReader('035720', '2017')

print(kakao)

open_values = kakao[['Open']]  # 장 시작시 금액

scaler = MinMaxScaler(feature_range=(0, 1))  # 0 ~ 1 사이의 값으로 Regularization
scaled = scaler.fit_transform(open_values)

WINDOW_SIZE = 30
TEST_SIZE = 100
train_data = scaled[:-TEST_SIZE]
test_data = scaled[-TEST_SIZE:]

X_train, y_train = make_sample(train_data, WINDOW_SIZE)

model = Sequential()

'''LSTM'''
# model.add(
# 	LSTM(
# 		16
# 		, input_shape=(X_train.shape[1], 1)
# 		, activation='tanh'
# 		, return_sequences=False
# 	)
# )

'''one RNN'''
# model.add(
#   SimpleRNN(
# 	    16
#   	, input_shape=(X_train.shape[1], 1)
# 	    , activation='tanh'
#   )
# )

'''two RNN'''
model.add(
	SimpleRNN(
		16
		, activation='tanh'
		, input_shape=(X_train.shape[1], 1)
	)
)

model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=16)

X_test, y_test = make_sample(test_data, 30)
pred = model.predict(X_test)

plt.figure(figsize=(12, 9))
plt.plot(y_test * scaler.data_max_, label='stock price')
plt.plot(pred * scaler.data_max_, label='predicted stock price')
print(f'scale: {scaler.data_max_}')

pred_n = pred * scaler.data_max_
y_test_n = y_test * scaler.data_max_

print(f'# RMSE {np.mean(losses.mean_squared_error(pred_n, y_test_n) ** 0.5)}')
print(f'# X_train y_train shape {X_train.shape}, {y_train.shape}')
print(f'# X_test y_test shape {X_test.shape}, {y_test.shape}')

plt.legend()
plt.show()

"""
카카오 주가: 2017년부터 데이터 이용

데스트 데이터 : 후반부 100개 사용
"""
