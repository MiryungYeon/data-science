# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

"""

print('hello')

# 한줄 주석
""" 여러줄 주석 """

a = 'Now is better than never'
print(type(a)) # Python은 인터프린터 언어이기 때문에 모든 변수는 클래스 <class 'str'>
a # print() 뒤에 쓸 때만 허용, print() 앞에 쓸 경우, 출력 X

a[-1]

print(a.find('N',3)) # 존재하지 않는 경우 -1
a.index('o') # 문자의 위치 반환

a.count('e') # 'e'의 개수

b = "1234"
c = b.join('ABCD') # 각 문자 사이에 b가 삽입
c

d = ' p '
d.lstrip() # 왼쪽 공백 제거

listA = [0,1,2,3,4,5,6,7]
print(listA)
print(type(listA))
print(listA[2])
print(listA[-1])

listB = [1,2,[3,'4']]
print(listB)
print(listB[2])
print(listB[2][1])

listA, listB # Tuple

listA + listB # List

listA[1] + listB[2][0] # Slicing = 리스트, Indexing = 원소 → 둘은 더할 수 없음

listA[3:] + listB[0:]

print(listA)
listA[0:3] = ['a','b'] # 대체
print(listA)
listA[-1] = 'c'
print(listA)

listA.append('d')

listA

listA[1] = '2'

listA

print(listA*2) # List 형태

del listA[1]

listA

print(listA.pop(-1))

listA

listA.count(3)

tupleA=(1,2,3)
print(tupleA)
print(type(tupleA))

tupleA[2]

dict = {'name':['Kim',['An','Yeon']],'phone':'0212345678','birth':'0923'}
dict

dict['name'][1]

dict['name']

list(dict.keys())

list(dict.values())