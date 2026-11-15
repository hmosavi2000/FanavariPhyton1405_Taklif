# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:28:14 2026

@author: hmosa
"""

students=[('Ali',22,18),('Sara',20,15),('Reza',23,9),('Mina',21,20),('Nima',19,12),('Amir',24,7)]

f=0
for i in range(0,len(students)):
  print('Name:',students[i][0],' -Age:',students[i][1],' -Score:',students[i][2])
    
'''
Name: Ali  -Age: 22  -Score: 18
Name: Sara  -Age: 20  -Score: 15
Name: Reza  -Age: 23  -Score: 9
Name: Mina  -Age: 21  -Score: 20
Name: Nima  -Age: 19  -Score: 12
Name: Amir  -Age: 24  -Score: 7
'''

#===========================================
for i in range(0,len(students)):
    if students[i][2]<10:
        print(students[i][0])
        
'''
Reza
Amir

'''
#===========================================
a=0
for i in range(0,len(students)):
    a=a+students[i][2]
    
print('Average:',a/len(students))

'''
Average: 13.5
'''

#===========================================

b=0
c='0'
for i in range(0,len(students)):
    if b<students[i][2]:
        b=students[i][2]
        c=students[i][0]
    
print(c)     #Mina

#===========================================

a=0
for i in range(0,len(students)):
    a=a+students[i][2]
    
av=a/len(students)

for i in range(0,len(students)):
    if students[i][2]>av:
        print(students[i][0])
        
'''
Ali
Sara
Mina

'''