# -*- coding: utf-8 -*-
"""
Created on Mon May 29 23:50:20 2023

@author: CHIBUZOR
"""


# GRID TRAVELLER PROBLEM 

"""
Say that you are a traveller on a 2D grid, you begin in the top-left corner and 
your goal is to travel to the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m x n?

Write a function `gridTraveler(m, n)` that calculates this.

"""

# SOLUTION

import time

start = time.time()

def gridTraveler(m, n, memo={}):
    key = str(m) + "," + str(n)
    
    if(key in memo):
        return memo[key]
        
    if(m == 0 or n == 0):
        return 0
    
    if(m == 1 and n == 1):
        return 1
    
    memo[key] = gridTraveler(m - 1, n) + gridTraveler(m, n - 1)
    
    return memo[key]

print(gridTraveler(2, 1))
print(gridTraveler(4, 8))
print(gridTraveler(6, 5))
print(gridTraveler(18, 18))
print(gridTraveler(200, 100))
print(gridTraveler(2000, 1000))

print("Time consumed: ", time.time() - start)    

