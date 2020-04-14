#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:59:42 2020

@author: ctralie
"""


# 4! = 4*3*2*1 = 24
# 6! = 6*5*4*3*2*1 = 720

def fac_loop(n):
    res = 1 # Accumulator
    for i in range(1, n+1):
        res = res*i
    return res

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)
    
print(4, fac(4))
print(6, fac(6)) 
