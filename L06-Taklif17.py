# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:05:49 2026

@author: hmosa
"""

def count_with_while(start,end):
    i=start
    b=[]
    while i<=end:
        b.append(i)
        i+=1
    return b

c=count_with_while(1,20)
print(c)

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]