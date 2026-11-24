# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:49:35 2026

@author: hmosa
"""
def sum_until_zero(max_count):
    a=0
    count=0
    for i in range(1,max_count):
        a=int(input(f'Enter Number{i}:'))
        if a==0:
            break
        else:
            count=a+count
    return count
     
c=sum_until_zero(10)
print(c)

'''
Enter Number:1
Enter Number:2
Enter Number:3
Enter Number:4
Enter Number:5
Enter Number:6
Enter Number:7
Enter Number:8
Enter Number:9
Enter Number:10
55

'''


'''
Enter Number:1
Enter Number:2
Enter Number:3
Enter Number:0
6
'''