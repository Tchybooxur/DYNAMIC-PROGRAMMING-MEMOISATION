# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:42:15 2023

@author: CHIBUZOR

QUESTION:
Write a funtion `howSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return an array containing any combination of elements
that add up to exactly the targetSum. If there is no combination that adds up
to the targetSum, then return null. 

If there are multiple combintions possible, you may return any single one.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.


Test cases:
    print(howSum(7, [2, 3]))  # [3, 2, 2]
    print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
    print(howSum(7, [2, 4]))  # None
    print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print(howSum(300, [7, 14]))  # None

"""

def howSum(targetSum, numbers, memo=None):
    if(memo == None): memo = {}
    
    # Memo base case
    if (targetSum in memo): return memo[targetSum]
    
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    
    for number in numbers:
        diff = targetSum - number
        diffResult = howSum(diff, numbers, memo)
        if (diffResult != None):
            memo[targetSum] = [*diffResult, number]
            return memo[targetSum]
        
    memo[targetSum] = None
    return None

"""
Brute force complexities:
    m = targetSum
    n = len(numbers)
Time complexity -> O(n^m * m)    
Space complexity -> O(m)   
___________________________________________

Memoised complexities: 
    m = targetSum
    n = len(numbers)
Time complexity -> O(n*m^2)
Space complexity -> O(m^2)

"""

print(howSum(7, [2, 3]))  # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7]))  # [4, 3]
print(howSum(7, [2, 4]))  # None
print(howSum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(howSum(300, [7, 14]))  # None
    
    
    
    
    
    
    
    
    
    
    
    
    
    