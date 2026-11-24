# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def odd_number(num1,num2):
    odd=[]
    for i in range(num1,num2):
        if i%2!=0:
           odd.append(i)
           
    return odd
       
        
a=odd_number(10, 50)

print(a)