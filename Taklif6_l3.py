# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:15:26 2026

@author: hmosa
"""

print(30*'=')
Product_Name=input('Product Name:').strip().title()
Price=float(input('Product Price:'))
Discount=input('Discount Code:').upper()
if Discount=='PYTHON20':
    NewPrice=0.8*Price
    print(NewPrice)
    
if Discount!='PYTHON20':
    print(Price)