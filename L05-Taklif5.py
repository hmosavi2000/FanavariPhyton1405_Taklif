# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:48:31 2026

@author: hmosa
"""

numbers=[12,7,25,18,3,40,11,8]

for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        print(numbers[i])
'''
12
18
40
8'
'''
#=====================================        
count=0
for i in range(0,len(numbers)):
    if numbers[i]%2==0:
       count=count+1
       
print(count) #4


#=====================================        
a=[]
for i in range(0,len(numbers)):
    if numbers[i]%2==0:
       a.append(numbers[i])
       
print(a) #[12, 18, 40, 8]


