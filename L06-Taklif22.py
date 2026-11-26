# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:26:03 2026

@author: hmosa
"""

def login_coditional(correct_password):
    adminPass='python123'
 
    while  adminPass!=correct_password:
        correct_password=input('Enter Password:')
        if adminPass==correct_password:
            return 'True'
        
c=login_coditional(input('Enter Password:'))

if c=='True':   
    print('Login Successful')
    
    
#=========================================
def login_break(correct_password):
    adminPass='python123'
 
    while  True:
        
        if adminPass==correct_password:
            return 'True'
            break
        else:
            correct_password=input('Enter Password:')
        
c=login_coditional(input('Enter Password:'))

if c=='True':   
    print('Login Successful')
'''
Enter Password:hamed
Enter Password:dsf
Enter Password:gbfr
Enter Password:python123
Login Successful
'''