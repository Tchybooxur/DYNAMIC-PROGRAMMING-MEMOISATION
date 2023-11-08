# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:43:36 2023

@author: CHIBUZOR

Write a funtion `countConstruct(target, wordBank)` that accepts a target string and an array
of strings as arguments.

The function should return the number of ways that the `target` can be constructed
by concatenating elements of the `wordBank` array.

You may reuse elements of `wordBank` as many times as needed.

Test cases:
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", 
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
"""


def countConstruct(target, wordBank, memo=None):

    # Hedge memo from misbehaviour
    if (memo == None):
        memo = {}

    # memo base case
    if (target in memo):
        return memo[target]

    # Brute force base case
    if (target == ""):
        return 1

    count = 0

    for word in wordBank:
        if(target.find(word) == 0):
            suffix = target[len(word):]
            count += countConstruct(suffix, wordBank, memo)
    memo[target] = count
    return count


""""
NB: You didnt need to worry about what is returned when it's not 1 because the code;
if-statement in the for-loop is only concerned about the path that leads to an empty
string ie path that returns 1. That other path is not traversed.
"""

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(countConstruct("skateboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                     ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
