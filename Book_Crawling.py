# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

"""

import urllib.request
import json
import pandas as pd
#client_id = "client_id"
#client_secret = "client_secret"

"""encText = urllib.parse.quote("파이썬") # 문자 URL 인코딩
url = "https://openapi.naver.com/v1/search/book?query=" + encText + "&start=1&display=5" # json 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    results = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)"""

#result = json.loads(results)
#result

def create_url(search_type, search_text, start_num, display_num):
  base = "https://openapi.naver.com/v1/search/"
  node = search_type + ".json"
  param_query = "?query=" +urllib.parse.quote(search_text)
  param_start = "&start="+str(start_num)
  param_display = "&display="+str(display_num)

  return base + node + param_query + param_start + param_display

# 호출
create_url("book", "python", 1, 10)

url = create_url("book", "python", 2, 5)

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

result = json.loads(response.read().decode('utf-8'))
result

len(result['items'])

titles = [result['items'][n]['title'] for n in range(0,10)]
titles

authors = [result['items'][n]['author'] for n in range(0,10)]
authors

pubdates = [result['items'][n]['pubdate'] for n in range(0,10)]
pubdates

df = pd.DataFrame({"책제목":titles,"작가이름":authors,"출판일":pubdates})
df

def get_dataframe(url):
  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)

  response = urllib.request.urlopen(request)

  result = json.loads(response.read().decode('utf-8'))

  end_num = result['display']

  titles = [result['items'][n]['title'] for n in range(end_num)]
  authors = [result['items'][n]['author'] for n in range(end_num)]
  pubdates = [result['items'][n]['pubdate'] for n in range(end_num)]

  return pd.DataFrame({"책제목":titles, "작가":authors, "출판일": pubdates})

url = create_url("book","빅데이터",1,10)
get_dataframe(url)

[n for n in range(1,300,100)] # List

result_search = []

for n in range(1,300,100):
  url = create_url("book", "머신러닝", n, 100)
  result_search.append(get_dataframe(url))

result_search = pd.concat(result_search)
result_search

# Pandas Table
#pd.set_option('display.max_rows',None)
# Pandas Reset
pd.reset_option('^display.', silent=True)

result_search = []
def get_naversearch(search_type, search_text, total_num, display_num):
  for n in range(1, total_num, display_num):
    url = create_url(search_type, search_text, n, display_num)
    result_search.append(get_dataframe(url))
  return pd.concat(result_search)

f_result = get_naversearch("book", "딥러닝", 300, 100)

f_result

f_result.head()

f_result.tail()

f_result.info()

f_result.to_excel('book.xlsx', sheet_name='Sheet1')