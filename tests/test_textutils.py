from textutils_bibekbhatta import reverse, is_palindrome, count_vowels, capitalize_words

# Quick self-test
assert reverse("bibek") == "kebib"
assert is_palindrome("racecar") == True
assert is_palindrome("hello") == False
assert count_vowels("hello") == 2
assert capitalize_words("bibek bhatta") == "Bibek Bhatta"
print("All tests passed! Your library is working.")