# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:58:42 2026

@author: hmosa
"""

numbers=[2,4,6,8,10]

def square_numbers(numbers):
    a=[]
    
    for i in numbers:
        a.append(i**2)
    return(a)
c=square_numbers(numbers)
print(c) #[4, 16, 36, 64, 100]
