# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:47:47 2026

@author: hmosa
"""
def skip_multiples_of_three(start,end):
    a=[]
    for i in range(start,end):
        if i%3==0:
            continue
        else:
            a.append(i)
    return a

c=skip_multiples_of_three(1,30)
print(c)
        
'''
[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]'''