# This Code will predict Stock Clossing Price using LSTM Method
# Author: Shahriar_panda

import pandas as pd
import numpy as np
import math
import pandas.io as wb
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt

df = wb.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2020-02-21')
print(df)
print(df.shape)

plt.figure(figsize=(16, 8))
plt.title('Close Price History')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()

data = df.filter(['Close'])
dataset = data.values
data_train_len = math.ceil(len(dataset) * .8)
print(data_train_len)

scaler = MinMaxScaler(feature_range=(0, 1))
data_scale = scaler.fit_transform(dataset)
print(data_scale)

train_data = data_scale[0:data_train_len:1]
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i - 60: i, 0])
    y_train.append(train_data[i, 0])
    if i <= 60:
        print(x_train)
        print(y_train)
