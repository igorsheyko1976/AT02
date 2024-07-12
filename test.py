import pytest
from main import count_vowels

def test_only_vowels():
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0

def test_mixed_string():
    assert count_vowels("Hello World") == 3
    assert count_vowels("Python Programming") == 4
    assert count_vowels("AEiou BCDFg") == 5

if __name__ == "__main__":
    pytest.main()
