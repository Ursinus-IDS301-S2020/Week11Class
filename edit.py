#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ex)

c  h  r  i  s. 
c  h  a  s  e. 

Way #3:
Match c to c: cost 0
Match h to h: cost 0
Match r to a: cost 1
Delete i: cost 1
Match s to s: cost 0
Delete e: cost 1 

Way #1:
Match c to c: cost 0
Match h to h: cost 0
Delete r: cost 1
Match i to a: cost 1
Match s to s: cost 0
Delete e: cost 1
Total cost: 3

Way #2:
match c to c
match h to h
match r to a (1)
match i to s (1)
match s to e (1)
Total cost: 3

dist("chris", "chris") = 0
dist("chris", "chase") > 0

1) Match characters.  If they're the same
   I don't pay a cost. If they're different
   pay a cost of 1
2) Delete a character at a cost of 1



Ex) school  fools

s  c  h  o  o  l.
f  o  o  l.  s

Delete s (cost 1)
Delete c (cost 1)
Match h to f (cost 1)
Match o to o 
Match o to o
Match l to l
Delete s (cost 1)
Cost 4



"""


"""
How to solve edit distance recursively

fib(n) = fib(n-1) + fib(n-2)

edit("chris", "chase") = min(
    1 + edit("chri", "chase"), // Deleted s from "chris"
    1 + edit("chris", "chas"), // Deleted e from "chase"
    1 + edit("chri", "chas") // Match e to s
    )
    
edit("chri", "chase") = min(
                         1 + edit("chr", "chase")
                         1 + edit("chri", "chas")
                         1 + edit("chr", "chas")
                         )
Stopping condition:
edit("", "chas")
edit("", s) = # characters in s

"""

def edit(a, b):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    # Delete the last character from a
    cost1 = 1 + edit(a[0:-1], b)
    # Delete the last character from b
    cost2 = 1 + edit(a, b[0:-1])
    # Match the last character from a to last in b
    cost3 = 0 + edit(a[0:-1], b[0:-1])
    if a[-1] != b[-1]:
        cost3 += 1
    return min(cost1, cost2, cost3)

print(edit("school", "fools"))
