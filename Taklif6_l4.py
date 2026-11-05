# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:12:50 2026

@author: hmosa
"""

print(30*'=')
Users=['ali','hasan','taha','hamed']
User=input('Enter Your User:')
Pass=input('Enter Your Password:')

if User.lower() in Users:
    if Pass.lower()=='python123':
        print('----Welcome---')
    else:
        print('password incorrect!!!!')

else:
    print('User not allowed')
    
