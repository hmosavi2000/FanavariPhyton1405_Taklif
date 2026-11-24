# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:30:39 2026

@author: hmosa
"""
def reverse_count(start,end):
    a=[]
    for i in range(start, end, -1):
        a.append(i)
    return a

b=reverse_count(20, 1)
print(b)