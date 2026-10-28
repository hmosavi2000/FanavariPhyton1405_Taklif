# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:00:38 2026

@author: hmosa
"""

#==========================
print(30*'=')
score=[15,18,12,20,16]

score.append(19)
print(score)
print(30*'=')
score.remove(12)
print(score)
print(30*'=')
score[1]=17
print(score)
print(30*'=')
score.insert(2, 14)
print(score)
print(30*'=')
score.sort()
print(score)
print(30*'=')
score.reverse()
print(score)
print(30*'=')
print(len(score))

