# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:59:26 2023

@author: CHIBUZOR


QUESTION:
    
Write a funtion `bestSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return an array containing the shortest combination of numbers
that add up to exactly the targetSum. 

If there is any tie for the shortest combination, you may return any one of the shortest.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.


Test cases:
    print(bestSum(7, [5, 3, 4, 7]))  # [7]
    print(bestSum(8, [2, 3, 5]))  # [3, 5]
    print(bestSum(8, [1, 4, 5]))  # [4, 4]
    print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]

"""


def bestSum(targetSum, numbers, memo=None):
    
    # Hedge memo from misbehaving
    if (memo == None): memo={}
    
    shortestCombination = None
    
    if (targetSum == 0): return []
    if (targetSum < 0): return None
    if (targetSum in memo): return memo[targetSum]
    
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum(remainder, numbers, memo)
        if (remainderCombination != None):
            combination = [*remainderCombination, number]
            if (shortestCombination == None or (len(combination) < len(shortestCombination))):
                shortestCombination = combination
    
    memo[targetSum] = shortestCombination
    return shortestCombination


print(bestSum(7, [5, 3, 4, 7]))  # [7]
print(bestSum(8, [2, 3, 5]))  # [3, 5]
print(bestSum(8, [1, 4, 5]))  # [4, 4]
print(bestSum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]


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
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
