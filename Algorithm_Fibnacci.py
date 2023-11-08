# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:11:41 2023

@author: CHIBUZOR
"""
import time

# Finding nth term fibonacci

fibonacci_cache = {}

def fibonacci(n):
    # if value is cached, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # compute nth term
    if(n == 1):
        value = 1
    elif(n == 2):
        value = 1
    elif(n > 2):
        value = fibonacci(n-1) + fibonacci(n-2)
    # cache the value and return it  
    fibonacci_cache[n] = value
    return value

def fiboo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

start = time.perf_counter()
for i in range(1, 501):
    print(i, " : ", fibonacci(i))
end = time.perf_counter()
print()
print(f"Fibonacci function finished in {end-start} seconds.")
print()

start = time.perf_counter()
for i in range(1, 501):
    print(i, " : ", fiboo(i))
end = time.perf_counter()
print()
print(f"Fiboo function finished in {end-start} seconds.")

    
