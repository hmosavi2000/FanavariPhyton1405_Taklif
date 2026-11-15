# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:21:20 2026

@author: hmosa
"""

users=[(1,'ali','active'),(2,'sara','inactive'),(3,'reza','active'),(4,'mina','inactive'),(5,'nima','active')]

a=input('Enter Username:').lower()
f=0
for i in range(0,len(users)):
   if users[i][1]==a:
       print('ID:',users[i][0],'-Status:',users[i][2])
       f=1
       break
    
if f==0:
    print('Not Found!!!!!!')
    
    
'''
Enter Username:sara
ID: 2 -Status: inactive

Enter Username:hamed
Not Found!!!!!!

'''