# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:21:20 2026

@author: hmosa
"""

users=[(1,'ali','active'),(2,'sara','inactive'),(3,'reza','active'),(4,'mina','inactive'),(5,'nima','active')]

a=input('Enter Username:').lower()
def search_user(users,username):
    f=0
    a=[]
    for ID,name,ac in users:
       if name==username:
           a.append(f'{name}:{ac}')
           f=1
           break
    return f,a
    
c=search_user(users,a)
if c[0]==0:
    print('Not Found!!!!!!')
else:
    print(c[1])
    
    
'''
Enter Username:sara
ID: 2 -Status: inactive

Enter Username:hamed
Not Found!!!!!!

'''