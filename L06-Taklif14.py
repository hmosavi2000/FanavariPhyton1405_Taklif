# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:08:51 2026

@author: hmosa
"""

products=[('Laptop',50000,2),('Mouse',800,3),('Keyboard',1500,2),('Monitor',12000,1)]

def calculate_cart(products):
    a=0
    b=[]
    for name,price,total in products:
        c=price*total
        b.append(f'Product:{name}:{c}')
        a=a+c
    return b,a
    
d=calculate_cart(products)
print(d[0])
print('Sum=',d[1])
    
'''
['Product:Laptop:100000', 'Product:Mouse:2400', 'Product:Keyboard:3000', 'Product:Monitor:12000']
Sum= 117400
'''