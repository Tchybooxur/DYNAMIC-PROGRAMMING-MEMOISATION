# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:44:13 2023

@author: CHIBUZOR

Write a funtion `allConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return a 2D array containing all of the ways that the `target` 
can be constructed by concatenating elements of the `wordBank` array. Each element of the 
2D array should represent one combination that constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) 
    # [
    #    ["purp", "le"],
    #    ["p", "ur", "p", "le"],
    # ]
    
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])) 
    # [
    #    ["ab", "cd", "ef"],
    #    ["ab", "c", "def"],
    #    ["abc", "def"],
    #    ["abcd", "ef"]
    # ]
    
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) 
    # []
    
    print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"])) 
    # []
    
"""


def allConstruct(target, wordBank, memo=None):

    # Hedge memo from misbehaviour
    if (memo == None):
        memo = {}

    # memo base case
    if (target in memo):
        return memo[target]

    # brute force base case
    if (target == ""):
        return [[]]

    result = []

    for word in wordBank:
        if (target.find(word) == 0):
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = list(map(lambda ways: [word, *ways], suffixWays))
            result += targetWays

    memo[target] = result
    return result


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#    ["purp", "le"],
#    ["p", "ur", "p", "le"],
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# [
#    ["ab", "cd", "ef"],
#    ["ab", "c", "def"],
#    ["abc", "def"],
#    ["abcd", "ef"]
# ]

print(allConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# []

print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaz",
      ["a", "aa", "aaa", "aaaa", "aaaaa"]))
# []


'''
Space-Time complexities:
    m = len(target)
    n = len(wordBank)
Time complexity -> O(n^m)    
Space complexity -> O(m)  
'''
