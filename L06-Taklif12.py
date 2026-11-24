# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:56:24 2026

@author: hmosa
"""

students=[('Ali',22),('Sara',19),('Reza',25),('Nima',20),('Mina',23)]

def format_students(students):
    b=[]
    for name,age in students:
        b.append(f'(Name:{name},Age:{age})')
    return b
    
c=format_students(students)

print(c)
'''
['(Name:Ali,Age:22)', '(Name:Sara,Age:19)', '(Name:Reza,Age:25)', '(Name:Nima,Age:20)', '(Name:Mina,Age:23)']
'''