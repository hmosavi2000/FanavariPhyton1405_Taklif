# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:44:34 2026

@author: hmosa
"""

def user_management_menu(Users):
    customUser=[]
    while True:
        print('1-Add User \n 2-Show Users \n 3-Search User: \n 4-Exit')
        print(10*'-')
        User_Choice=int(input('Enter Menu Number:'))
        if User_Choice==1:
            print(10*'-')
            b=input('Enter New User:')
            customUser.append(b)
            print('User Added')
            print(10*'-')
        elif  User_Choice==2:
            print(customUser)
        elif  User_Choice==3:
             print(10*'-')
             b=input('Enter User for searching:')
             if b in customUser:
                 print('User Found')  
                 print(10*'-')
             else:
                print('Invalid User!!!!!')
                print(10*'-')
        elif User_Choice==4:
            break
        else :
            print('Wrong Number')
            print(10*'-')
            

user_management_menu([])     
            
'''
1-Add User 
 2-Show Users 
 3-Search User: 
 4-Exit
----------
Enter Menu Number:1
----------
Enter New User:hamed
User Added
----------
1-Add User 
 2-Show Users 
 3-Search User: 
 4-Exit
----------
Enter Menu Number:1
----------
Enter New User:ali
User Added
----------
1-Add User 
 2-Show Users 
 3-Search User: 
 4-Exit
----------
Enter Menu Number:2
['hamed', 'ali']
1-Add User 
 2-Show Users 
 3-Search User: 
 4-Exit
----------
Enter Menu Number:3
----------
Enter User for searching:hamed
User Found
----------
1-Add User 
 2-Show Users 
 3-Search User: 
 4-Exit
----------
Enter Menu Number:4

'''