# -*- coding: utf-8 -*-
"""


Automatically generated by Colaboratory.


"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='ignore')

df = sns.load_dataset('mpg')

df.info()

df

df['origin'].unique()

df.isnull().sum()

df = df.dropna()

df.isna().sum()

df.drop('name', axis=1, inplace=True)

df

df.drop('origin', axis=1, inplace=True)

df

X = df.drop('mpg', axis=1, inplace=False)

Y = df['mpg']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, random_state=0)

lr = LinearRegression()

lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)

Y_test

mse = mean_squared_error(Y_test, Y_predict)

np.sqrt(mse)

plt.figure(figsize=(10, 10))
plt.subplot(2, 3, 1)
sns.regplot(x='cylinders', y='mpg', data=df, color='r')
plt.subplot(2, 3, 2)
sns.regplot(x='displacement', y='mpg', data=df, color='g')
plt.subplot(2, 3, 3)
sns.regplot(x='horsepower', y='mpg', data=df, color='b')
plt.subplot(2, 3, 4)
sns.regplot(x='weight', y='mpg', data=df, color='c')
plt.subplot(2, 3, 5)
sns.regplot(x='acceleration', y='mpg', data=df, color='m')
plt.subplot(2, 3, 6)
sns.regplot(x='model_year', y='mpg', data=df, color='y')

cylinders_1 = int(input('cylinders : '))
displacement_1 = int(input('displacement : '))
horsepower_1 = int(input('horsepower : '))
weight_1 = int(input('weight : '))
acceleration_1 = int(input('acceleration : '))
model_year_1 = int(input('model_year : '))

lr.predict([[cylinders_1, displacement_1, horsepower_1, weight_1, acceleration_1, model_year_1]])