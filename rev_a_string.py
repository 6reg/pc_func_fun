"""
This program takes in a string and returns the characters in reverse order
"""

def get_reversed_string(s):
    reversed = ""
    for ch in s:
        reversed = ch + reversed
    return reversed

print(get_reversed_string("A man, a plan, Panama"))
print(get_reversed_string("Hello"))
print(get_reversed_string("This that the other"))
