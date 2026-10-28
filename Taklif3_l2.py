# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:27:16 2026

@author: hmosa
"""

#===========================================
print (30*'-')
ProName=input('Name Mahsol?:')
Price=input('Gheymat?:')
discount=input('Darsad Takhfif?:')
new_Price=float(Price)-(float(Price)*(float(discount)/100))
print('Mahsool:----',ProName.upper().strip()+':',new_Price)

'''
Name Mahsol?:  laptop   
Gheymat?:3000
Darsad Takhfif?:2
Mahsool:---- LAPTOP: 2940.0'''