# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:54:53 2020

@author: anshu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset_train = pd.read_csv("dataset_train.csv")
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()
scaled_training = sc.fit_transform(dataset_train)
x_train = []
y_train = []
for i in range(4,162):
    x_train.append(scaled_training[i-4:i,0])
    y_train.append(scaled_training[i,0])
x_train,y_train = np.array(x_train),np.array(y_train)
x_train.shape
x_train.ndim
x_train = np.reshape(x_train ,(158,4,1))
x_train.shape[1]
x_train.ndim
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
model = Sequential()
model.add(LSTM(units = 4 , return_sequences = True , input_shape = (4,1)))
model.add(Dropout(0.2))
model.add(LSTM(units = 4 , return_sequences = True ))
model.add(Dropout(0.2))
model.add(LSTM(units = 4 , return_sequences = True ))
model.add(Dropout(0.2))
model.add(LSTM(units = 4))
model.add(Dropout(0.2))
model.add(Dense(units = 1))
model.compile(optimizer = 'adam',loss = 'mse',metrics = ['mse'])
model.fit(x_train,y_train,epochs = 2000,batch_size = 16)

model.save("predict.h5")
