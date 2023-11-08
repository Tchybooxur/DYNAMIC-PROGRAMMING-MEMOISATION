# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:59:18 2023

@author: CHIBUZOR

QUESTION:
    
Write a funtion `canConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return a boolean indicating whether or not the `target` can be constructed
by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # True
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False

"""


def canConstruct(target, wordBank, memo=None):

    # Hedge memo from acting funny
    if (memo == None):
        memo = {}

    # Memo base case
    if (target in memo):
        return memo[target]

    # Brute force base case
    if (target == ""):
        return True

    for word in wordBank:
        if (target.find(word) == 0):
            suffix = target[len(word):]
            if (canConstruct(suffix, wordBank, memo) == True):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(canConstruct("skateboard", ["bo", "rd",
      "ate", "t", "ska", "sk", "boar"]))  # False
print(canConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                   ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False

"""
Brute force complexities:
    m = len(target)
    n = len(wordBank)
Time complexity -> O(n^m * m)    
Space complexity -> O(m^2)   
___________________________________________

Memoised complexities: 
    m = len(target)
    n = len(wordBank)
Time complexity -> O(n*m^2)
Space complexity -> O(m^2)

"""
