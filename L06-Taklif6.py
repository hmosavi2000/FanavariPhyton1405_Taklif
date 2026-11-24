# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:54:29 2026

@author: hmosa
"""

scores=[15,18,12,20,16,14,19]

def calculate_scores(scores):
    a=0
    for i in scores:
        a=i+a
        
    b=a/len(scores)
    return a,b
  
c=calculate_scores(scores)
print('sum=',c[0]) #sum= 114
print('Avarage=',c[1]) #Avarage= 16.285714285714285

#=====================================        


