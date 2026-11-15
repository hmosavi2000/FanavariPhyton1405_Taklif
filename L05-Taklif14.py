# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:08:51 2026

@author: hmosa
"""

products=[('Laptop',50000,2),('Mouse',800,3),('Keyboard',1500,2),('Monitor',12000,1)]

a=0

for i in range(0,len(products)):
    print('Product:',products[i][0],'=',products[i][1]*products[i][2])
    a=a+(products[i][1]*products[i][2])
    
print('Sum=',a)
    
'''
Product: Laptop = 100000
Product: Mouse = 2400
Product: Keyboard = 3000
Product: Monitor = 12000
Sum= 117400
'''