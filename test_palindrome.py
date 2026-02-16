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
        is_palindrome(3.4)