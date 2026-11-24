# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:05:04 2026

@author: hmosa
"""

students=[('Ali',18),('Sara',12),('Reza',9),('Nima',20),('Mina',14)]

def filter_students_by_grade(students,min_grade):
    a=[]
    for name,score in students:
    
        if score>=min_grade:
            a.append(f'Name:{name}')
    return a

c=filter_students_by_grade(students,15)

print(c)
        
'''
Name: Ali
Name: Nima

'''