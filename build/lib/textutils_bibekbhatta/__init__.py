"""
textutils_bibekbhatta – Useful string functions by Bibek Bhatta
"""

def reverse(text):
    """Returns the reversed string."""
    return text[::-1]

def is_palindrome(text):
    """Returns True if the text reads same forward and backward (ignores spaces and capital letters)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(text):
    """Returns the number of vowels (a, e, i, o, u) in the text."""
    vowels = "aeiouAEIOU"
    total = 0
    for ch in text:
        if ch in vowels:
            total = total + 1
    return total

def capitalize_words(text):
    """Capitalizes the first letter of each word."""
    words = text.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return " ".join(capitalized_words)