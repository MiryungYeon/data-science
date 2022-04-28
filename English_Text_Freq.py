#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 자연어(텍스트) 데이터 전처리 : nltk(natural language toolkit)


# In[13]:


import re


# In[15]:


text = "I like an        $$ %& / apple"
text_mod = re.sub('[^a-zA-Z]+', ' ', text)
text_mod


# In[21]:


# 비식별화
text = "010-1234-5678 Kim"

text_mod = re.sub('^[0-9]{3}-[0-9]{4}-[0-9]{4}', '***-****-****', text) 
text_mod


# In[22]:


# 토큰화
import nltk


# In[23]:


nltk.download('punkt') # 토큰화와 관련된 Dataset
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4') # Open Multilingual Wordnet
# nltk.download('all')


# In[27]:


reWords = re.sub('[^a-zA-Z]+', ' ', 'I will make my              deep learning systems')
reWords


# In[28]:


# 토큰화
from nltk.tokenize import word_tokenize


# In[30]:


lreWords = reWords.lower()
reWordsToken = word_tokenize(lreWords) # 생성자, 인스턴스 생성
reWordsToken


# In[32]:


# 불용어(stopwords) 제거
from nltk.corpus import stopwords


# In[33]:


sWords = stopwords.words('English')


# In[34]:


reWordsTokenStop = [n for n in reWordsToken if n not in sWords]
reWordsTokenStop


# In[35]:


# 표제어 추출
from nltk.stem.wordnet import WordNetLemmatizer


# In[37]:


lemma = WordNetLemmatizer()


# In[38]:


reWordsTokenStopLema = [lemma.lemmatize(w) for w in reWordsTokenStop]
reWordsTokenStopLema


# In[39]:


# 람다(lambdat)식, 람다 함수 : 익명 함수를 지칭하는 용어


# In[42]:


def add(x, y):
    return x + y


# In[43]:


add(10, 20)


# In[46]:


f = lambda x, y: x + y
f([10], [20])


# In[45]:


(lambda x, y: x + y)(10, 20)


# In[47]:


[['hi', 'hello'], ['deep', 'computer'], ['machine', 'learning']] # 이차원 행렬 -> 일차원 행렬로 바꾸고 싶음, 차원 축소 reduce()


# In[54]:


from functools import reduce # 일반적으로 람다식 많이 사용
words = reduce(lambda x, y : x + y, [['hi'], ['hello', 'computer'], ['learning']])
words


# In[55]:


words.count('hi')


# In[56]:


from collections import Counter


# In[57]:


Counter(words)

