# -*- coding: utf-8 -*-
"""


Automatically generated by Colaboratory.


"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings(action='ignore')

colab_path='/content/drive/'
file_path = colab_path+'MyDrive/Colab/penguins.csv'

df = pd.read_csv(file_path, sep=',')
df

df.head()

df.info()

df.isna().sum()

df[df.isna().any(axis=1)]

df.dropna(how='all', subset=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'], inplace=True)
df[df.isna().any(axis=1)]

df.drop('sex', axis=1, inplace=True)

df.isna().sum()

df.shape

sns.pairplot(df, hue='species')

sns.pairplot(df, height = 5, vars = ['bill_length_mm', 'bill_depth_mm'], hue='species')

X = df[['bill_length_mm',	'bill_depth_mm',	'flipper_length_mm',	'body_mass_g']]
X



Y = df['species'].copy()

Y

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=0)

test_Y

DTC = DecisionTreeClassifier()

DTC.fit(train_X, train_Y)

Y_predict = DTC.predict(test_X)

Y_predict

test_Y

confusion_matrix(test_Y, Y_predict)

accuracy_score(test_Y, Y_predict)

DTC.predict([[5, 1.5, 3, 3.2]])

DTC.predict_proba([[5, 1.5, 3, 3.2]])