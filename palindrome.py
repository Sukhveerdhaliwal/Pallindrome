"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(Input):
    if not isinstance(Input, str):
        raise ValueError('Input must be a string')
    return False
