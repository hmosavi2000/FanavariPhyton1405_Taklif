# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:04:55 2026

@author: hmosa
"""

numbers=[4,9,15,23,42,56,71]
a=int(input('Enter Number:'))
flag=0
for i in range(0,len(numbers)):
    if a==numbers[i]:
        flag=1
        break
    
if flag==1:
    print('Number Found')
else:
    print('Not Found!!!!!')
    
'''
Enter Number:15
Number Found

Enter Number:23
Number Found
'''