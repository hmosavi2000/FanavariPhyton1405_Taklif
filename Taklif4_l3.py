# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:17:25 2026

@author: hmosa
"""

print(30*'=')
student=('Ali',21,'Tehran')
print(student[0])
a=list(student)
print(a)
print(type(a))
a[1]=22
print(a)
a[2]='Shiraz'
print(a)
student=tuple(a)
print(type(student))
