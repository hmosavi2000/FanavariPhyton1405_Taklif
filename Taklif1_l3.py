# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:18:09 2026

@author: hmosa
"""
#==========================
print(30*'=')
User_Str=input('Type string:')
print('all is numeric:',User_Str.isdigit())
print('all is letter:',User_Str.replace(' ', '').isalpha())
print('is AlphNumeric:',User_Str.isalnum())
print('is all UPPER:',User_Str.isupper())
if int(len(User_Str)>8):
    print('is lenght>8:True')
if int(len(User_Str)<8):
    print('is lenght>8:False')    
