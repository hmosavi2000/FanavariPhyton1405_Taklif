# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:06:47 2026

@author: hmosa
"""

print(30*'=')
No1=input('Enter Number:')
if No1.isnumeric():
    if int(No1)>0:
        print('Positive')
    elif int(No1)<0:
        print('Negetive')
else:
    print('----Not Number----')
    
    
    
#=====================================

print(30*'=')
No1=input('Enter Number:')
if No1.isnumeric():
    if int(No1)%2==0:
        print('EVEN')
    else:
        print('ODD')
else:
    print('----Not Number----')