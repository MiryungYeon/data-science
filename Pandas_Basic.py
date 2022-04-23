#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


s1 = pd.Series([10,20,30,90], name='a')
s1


# In[5]:


s1.index = ['a', 'b', 'c', 'd']
s1


# In[6]:


sr2 = pd.Series(data = [10,20,30,90], index = ['A','B','C','D'])
sr2


# In[8]:


sr3 = pd.Series({'C':20, 'D':50, 'E':100, 'F':90})
sr3


# In[11]:


sr3.index = ['2','3','5','10']
sr3


# In[12]:


sr3['2'] = 1000


# In[13]:


sr3


# In[17]:


df1 = pd.DataFrame({'A':10,'B':20,'C':50,'0':100},index=[0])
df1


# In[19]:


x = [1,3,4]
df11 = pd.DataFrame([x,[13,42,45],[135,234,789]], columns=['a','b','c'])
df11


# In[20]:


import numpy as np


# In[21]:


df2 = pd.DataFrame({'A':[np.nan, 10], 'B':['',20],'C':[100,50],'D':[80,90]})
df2


# In[22]:


1>3


# In[23]:


df2.isnull() # Boolean 


# In[24]:


df2.isna() # isnull()과 동일


# In[25]:


df2.replace('', np.nan, inplace=True)


# In[26]:


df2


# In[27]:


df2.fillna(0, inplace=True) # 결측값 0으로 변경
df2


# In[28]:


df3 = pd.DataFrame({'A':[np.nan, 10, 100, 20],'B':[20, 10, 100, 20],'C':[np.nan, 10, 100, np.nan],'D':[np.nan, 90, np.nan, 90]})


# In[29]:


df3


# In[30]:


df3.dropna(how='any', axis=0, inplace=True) # how='all'
# how = 'any'/'all'
# any -> row 또는 column에 NaN값이 1개만 있어도 Drop
# all -> row 또는 column에 모든 값이 NaN이어야 Drop

# axis = 0/1 or 'index'/'columns'
# 0 or 'index' -> NaN 값이 포함된 row를 Drop
# 1 or 'columns' -> NaN 값이 포함된 column을 Drop


# In[31]:


df3


# In[34]:


df4 = pd.DataFrame({'A':10, 'B':20, 'C':50, 'D':100}, index=[0])
df4.index = [1]
df4


# In[35]:


df5 = pd.DataFrame({'A':10, 'B':20, 'C':50, 'D':100}, index=[0])
df5


# In[36]:


df_add1 = pd.concat([df4, df5]) # Row를 +
df_add1


# In[39]:


df_add = df3 + df4 # 값을 +


# In[40]:


df_add


# In[46]:


df3['A']


# In[47]:


df3.A


# In[55]:


df_add1[0:2] # list slicing


# In[65]:


df_add1.loc[1]


# In[64]:


df_add1.iloc[0]


# In[66]:


# loc, iloc
# loc : 데이터프레임의 행이나 컬럼의 Label이나 Boolean array로 접근
# iloc : 데이터프레임의 행이나 컬럼에 Index 값으로 접근


# In[67]:


df_add1.loc[1, 'A']


# In[68]:


df_add1.loc[[1], ['A','B']] # DataFrame


# In[70]:


df_add1.loc[:, ['A','B']]


# In[71]:


df_add1.loc[:,:]


# In[73]:


df_add1.drop('A', axis=1)

