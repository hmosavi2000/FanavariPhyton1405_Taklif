# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:58:42 2026

@author: hmosa
"""

numbers=[2,4,6,8,10]

a=[]

for i in range(0,len(numbers)):
    a.append(numbers[i]**2)
    
print(a) #[4, 16, 36, 64, 100]