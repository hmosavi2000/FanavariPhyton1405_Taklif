# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:20:47 2026

@author: hmosa
"""

print(30*'=')
No1=int(input('Enter No1:'))
No2=int(input('Enter No2:'))
Oper=input('Enter Operation:')

if Oper=='*':
    print(No1*No2)
elif Oper=='/':
    print(No1/No2)
elif Oper=='-':
    print(No1-No2)
elif Oper=='+':
    print(No1+No2)