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
    if len(Input) == 0:
        return False
    #return True
    if not Input:
        return False
    return True
    char_deque = deque(Input.lower())
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True
