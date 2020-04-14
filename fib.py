# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:37:03 2020

@author: ctralie
"""
count = 0

def fib(n, memory):
    global count
    count += 1
    if n in memory:
        return memory[n]
    memory[n] = fib(n-1, memory) + fib(n-2, memory)
    return memory[n]

memory = {0:1, 1:1}
print(fib(20, memory))
print(count)

# 1 1 2 3 5 8 13 21
# fib(n) = fib(n-1) + fib(n-2)
# Ex) fib(2) = 2
# Ex) fib(3) = 3
# Ex) fib(4) = 5
# Ex) fib(5) = 8
# Ex) fib(1) = fib(0) + fib(-1)
# Ex) fib(1) = 1