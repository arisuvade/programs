"""Challenge: Palindrome Checker
Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome and False otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.

For example:

is_palindrome("racecar") should return True
is_palindrome("Hello") should return False
is_palindrome("A man, a plan, a canal, Panama") should return True
"""


from string import ascii_letters


def is_palindrome(word: str) -> bool:
    reversed_word: str = word[::-1].lower()
    w_letters: str = "".join(
        [letter for letter in word.lower() if letter in ascii_letters]
    )
    rw_letters: str = "".join(
        [letter for letter in reversed_word if letter in ascii_letters]
    )
    return rw_letters == w_letters


print(is_palindrome("racecar"))
print(is_palindrome("Hello"))
print(is_palindrome("A man, a plan, a canal, Panama"))
