# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:12:27 2026

@author: hmosa
"""


def custom_range(start,stop,step):
    i=start
    b=[]
    while i<=stop:
        b.append(i)
        i+=step
    return b

c=custom_range(1,20,2)
print(c)

#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]