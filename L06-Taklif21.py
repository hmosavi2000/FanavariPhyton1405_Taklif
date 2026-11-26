# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:19:57 2026

@author: hmosa
"""

def sum_until_zero_break():
    i=1
    nSum=0
    while True:
        b=int(input(f'Enter  Number{i}:'))
        if b==0:
            break
        else:
            nSum=nSum+b
            i+=1
    return nSum



c=sum_until_zero_break()
print('Total Sum:',c)

#===============================================


def sum_until_zero_conditional():
    b=int(input('Enter  Number1:'))
    i=1
    nSum=0
    while b!=0:
        i+=1
        nSum=nSum+b
        b=int(input(f'Enter  Number{i}:'))
       
    return nSum



c=sum_until_zero_break()
print('Total Sum:',c)



'''


Enter  Number1:12
Enter  Number2:14
Enter  Number3:51235
Enter  Number4:0
Total Sum: 51261

'''