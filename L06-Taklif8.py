# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:00:26 2026

@author: hmosa
"""

a=int(input('How many numbers to Enter:'))
def collect_numbers(count):
    b=[]
    
    for i in range(0,a):
        c=int(input(f'No{i}:'))
        b.append(c)
    return b

c=collect_numbers(a)
print(c)

'''
How many numbers to Enter:3
No:2
No:4
No:5
[2, 4, 5]
'''