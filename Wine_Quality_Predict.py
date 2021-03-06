# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colab_path = '/content/drive/'
file_path = colab_path+'MyDrive/ColabNotebooks/winequality-red.csv' # 바로 판다스로 변환

df_red = pd.read_csv(file_path, sep=';')
df_red

colab_path = '/content/drive/'
file_path = colab_path+'MyDrive/ColabNotebooks/winequality-white.csv' # 바로 판다스로 변환

df_white = pd.read_csv(file_path, sep=';')
df_white

df_red.columns == df_white.columns

df_red.insert(0, column='type', value='red')
df_red.head()

df_white.insert(0, column='type', value='white')
df_white.head()

wine = pd.concat([df_red, df_white])
wine

wine.shape

wine.info() # 정보

wine

# 종속변수 : 독립된 변수에 영향을 받는 변수, quality
# 독립변수 : 나머지 키 값

wine

# 회귀 Regression : 예측하고 싶은 종속변수가 숫자일 때
# 분류 Classification : 예측하고 싶은 종속변수가 이름(문자)일 때

# 열 이름의 공백 _
wine.columns = wine.columns.str.replace(' ','_')
wine.head()

wine.isnull().sum() # 결측치의 개수

wine.describe() # 기술 통계, 50%, 우리는 평균이 유효한지 아닌지 체크할 필요 -> 유의성 검사

wine.groupby('type')['quality'].describe()

wine.groupby('type')['quality'].agg('mean', 'std') # agg 모으다.

"""기초 통계 시각화 : Box Plot"""

import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams['figure.figsize'] = (4,3)
plt.rcParams['font.size'] = 12

data_a = wine[wine['type']=='red'].quality
data_b = wine[wine['type']=='white'].quality

fig, ax = plt.subplots()

ax.boxplot([data_a, data_b], notch=False, whis=1.5)
ax.set_ylim(-1.0, 10.0)
ax.set_xlabel('Wine Type')
ax.set_ylabel('Quality')

from scipy import stats

r_wine_q = wine.loc[wine['type']=='red', 'quality']
w_wine_q = wine.loc[wine['type']=='white', 'quality']

stats.ttest_ind(r_wine_q, w_wine_q, equal_var=False) # 두 타입의 개수가 같지 않으니까 False, P<0.05 유의적, e-24, 0이 앞에 24개 붙어있음

"""회귀 분석 모델 구축"""

import statsmodels.api as sm
import statsmodels.formula.api as smf

results = smf.ols('quality ~ fixed_acidity +	volatile_acidity	+	citric_acid	+	residual_sugar	+	chlorides	+	free_sulfur_dioxide	+	total_sulfur_dioxide	+	density	+	pH	+	sulphates	+	alcohol', data=wine).fit()

results.summary()

# wine.head(10) == wine[0:10]

sample = wine[0:10].drop(['type', 'quality'], axis=1)

results.predict(sample)