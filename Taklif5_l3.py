# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:24:58 2026

@author: hmosa
"""

print(30*'=')
student={'name':'Ali','Age':20,'City':'Tehran','Score':17}
print(student['name'],':',student['Score'])
student.update({'Age':21})
print(student)
student['university']='UT'
print(student)
student.update({'City':'Shiraz'})
print(student)
print(student.get('phone','Not Found'))
a=student.keys()
print(a)
b=student.values()
print(b)
print(student)




