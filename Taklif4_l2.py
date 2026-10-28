# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 23:27:31 2026

@author: hmosa
"""

#===========================================
print (30*'-')
Name=input('Enter your Name?:')
Count=input('Letters Count?:')
Name_Count=len(Name)
print(int(Count)== int(Name_Count))

'''
Enter your Name?:hamed
Letters Count?:3
False


Enter your Name?:hamed
Letters Count?:5
True
'''