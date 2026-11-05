# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:56:27 2026

@author: hmosa
"""


print(30*'=')
No1=input('Enter Sending Price:')

if int(No1)>=1000000:
        print('----FREE---')
elif int(No1)>=500000 and int(No1)<1000000 :
        print('Sending Code: 30000')
elif int(No1)<500000:
    print('Sending Code: 60000')