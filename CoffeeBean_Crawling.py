#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 커피빈 매장 정보 크롤링
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
import time

import warnings

warnings.filterwarnings(action='ignore')


# In[2]:


store_name = []
store_tel = []
store_add_c = []

for i in range(325, 330): # 테스트를 위해 일부 값만 세팅
    try:
        CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
        wd = webdriver.Chrome('chromedriver.exe')
        
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        
        wd.execute_script('storePop2(%d)' %i)
        time.sleep(1)
        
        html = wd.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        store_name_h2 = soup.select('div.store_txt>h2')
        store_name.append(store_name_h2[0].string)
        
        store_info = soup.select('table.store_table>tbody>tr>td')
        store_tel.append(store_info[3].string)
        
        store_address = store_info[2]
        store_add = list(store_address)
        store_add_c.append(store_add[0].strip()) # 공백 제거
    except:
        print(i)


# In[3]:


df_cb = pd.DataFrame({'매장이름':store_name, 'address':store_add_c, 'phone':store_tel})
df_cb

