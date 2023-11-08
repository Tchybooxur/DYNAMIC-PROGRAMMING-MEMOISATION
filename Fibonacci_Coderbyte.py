# -*- coding: utf-8 -*-
"""
Created on Tue May 23 17:11:44 2023

@author: CHIBUZOR
"""

# Finding nth term fibonacci

#fibonacci_cache = {}

def fibonacci(n, memo={}):
    # if value is cached, return it
    if (n in memo):
        return memo[n]
    # compute nth term
    if(n == 1):
        return 1
    elif(n == 2):
        return 1
    elif(n > 2):
        # cache the value and return it  
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


print(fibonacci(1000))

"""for i in range(1, 101):
    print(i, " : ", fibonacci(i))"""
