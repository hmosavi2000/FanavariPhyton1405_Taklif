# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:16:41 2026

@author: hmosa
"""

def get_valid_number():
    while True:
        b=int(input('Enter Valid Number(1-100):'))
        if b>=1 and b<=100:
            break
    return b

c=get_valid_number()
print(c)

'''
Enter Valid Number(1-100):101
Enter Valid Number(1-100):105
Enter Valid Number(1-100):53
53

'''