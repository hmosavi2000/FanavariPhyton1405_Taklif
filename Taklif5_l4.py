# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:03:47 2026

@author: hmosa
"""

print(30*'=')
Pass=input('Enter Your Password:')

if len(Pass)<8:
        print('Password is Short!!!!')
if Pass.isdigit() :
        print('Password is only DIGIT')
if ' ' in Pass :
    print('Password Has Space')