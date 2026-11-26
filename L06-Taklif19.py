# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:14:04 2026

@author: hmosa
"""


def sum_to_n_while(n):
    i=1
    b=0
    while i<=n:
        b=b+i
        i+=1
    return b

c=sum_to_n_while(5)
print(c) #15