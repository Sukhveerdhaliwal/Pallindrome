"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(Input):
    if not isinstance(Input, str):
        raise ValueError('Input must be a string')
    return False
    #return False
    #if len(Input) == 0:
        return False
    #return True
    if not Input:
        return False
    return True