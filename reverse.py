#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:23:27 2020

@author: ctralie
"""


## Take a string and reverse it
## Ex) circus,   sucric
def reverse_loop(s):
    srev = ""
    for i in range(len(s)):
        # i = 0,  c
        # i = 1,  ic
        # i = 2,  ric
        srev = s[i] + srev
    return srev
    
def reverse(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse(s[0:-1])


s = "circus"
print(s[::-1])
print(reverse(s))

# reverse("circus") = "s" + reverse("circu")