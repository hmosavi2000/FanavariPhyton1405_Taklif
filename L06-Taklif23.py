# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:33:13 2026

@author: hmosa
"""

def login_with_limit(correct_password,max_attemps):
    adminPass='admin123'
    i=max_attemps
   
    while  i>1:
        i=i-1
        if adminPass==correct_password:
            c='True'
            break
        else:
            
            
            correct_password=input(f'Enter Password(Max Attemp:{i}):')
            c='False'
    return c
            
        
c=login_with_limit(input('Enter Password:'),3)

if c=='True':   
    print('Login Successful')
else:
    print('Accoutn Locked!!!!!')
    
    
'''
Enter Password:dsfs
Enter Password(Max Attemp:2):sdf
Enter Password(Max Attemp:1):dsfs
Accoutn Locked!!!!!



Enter Password:fdsf
Enter Password(Max Attemp:2):admin123
Login Successful

'''

