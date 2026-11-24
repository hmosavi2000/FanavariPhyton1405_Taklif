# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:38:24 2026

@author: hmosa
"""
def multiplication_table(number):
   
    b=[]
    for i in range(1,11):
        f=number*i
        b.append(f'{number}*{i}={f}')
    return b

a=int(input('Enter Number:'))
c=multiplication_table(a)
print(c)
    
'''
Enter Number:
['5*1=5', '5*2=10', '5*3=15', '5*4=20', '5*5=25', '5*6=30', '5*7=35', '5*8=40', '5*9=45', '5*10=50']
'''