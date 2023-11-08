# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:20:22 2023

@author: CHIBUZOR


Alvin's (coderbyte on YouTube) memoization recipe:
1. Make it work:
    visualise the problem as a tree
    implement the tree using recursion
    test it
    
2. Make it efficient:
    add a memo object
    add a base case to return memo values
    store return values into the memo
_____________________________________________________________________________
    
QUESTION:
(CanSum Memoisation)
Write a funtion `canSum(targetSum, numbers)` that takes in a targetSum and an array
of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to
generate the targetSum using numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are nonnegative.    

"""

def canSum(targetSum, numbers, memo=None):
    if  (memo == None): memo = {}
    
    # Memo base case
    if (targetSum in memo): return memo[targetSum]    
    
    # write base cases
    if (targetSum == 0):
        #print("from return base case true: ", memo)
        return True
    
    if (targetSum < 0):
        #print("from return base case false: ", memo)
        return False
    
    # step through the list
    for number in numbers:
        difference = targetSum - number
        if (canSum(difference, numbers, memo) == True): 
            memo[targetSum] = True
            #print("from return for loop true: ", memo)
            return True
        
    memo[targetSum] = False
    # print("from return final false: ", memo)
    return False

print(canSum(7, [2, 3])) # True
print(canSum(7, [5, 3, 4, 7])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [2, 3, 5])) # True
print(canSum(300, [7, 14])) # False


    
