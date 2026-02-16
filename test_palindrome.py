"""
Tests the palindrome module
"""
import pytest

from palindrome import is_palindrome

def test_non_string_input_Raises_ValueErro():
    with pytest.raises(ValueError):
        is_palindrome(988)
    with pytest.raises(ValueError):
        is_palindrome([1,2,2])
    with pytest.raises(ValueError):
        is_palindrome(3.4)        is_palindrome(3.4)
        is_palindrome(3.4)
def test_empty_string_Input_returns_False():
    assert is_palindrome("") is False

def test_single_letter_returns_True():
    assert is_palindrome("a") is True

def test_double_letter_returns_True():
    '''Step 4: Assert that same character input Returns True'''
    assert is_palindrome("bb") is True

def test_nomatch_returns_False():
    assert is_palindrome("abc") is False

def test_laval_returns_True():
    """Step 6: Assert that "Laval" returns True"""
    assert is_palindrome("laval") is True
