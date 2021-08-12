def reverse_string(s):
    reversed = ""
    for i in s:
        reversed = i + reversed
    return reversed

def normalize(s):
    normalized = ""
    for ch in s:
        if ch.isalpha():
            normalized += ch.lower()
    return normalized

def is_palindrome(s):
    normalized = normalize(s)
    rev = reverse_string(normalized)
    return normalized == rev


print(is_palindrome("Hello"))
print(is_palindrome("A man, a plan, a canal - Panama!"))
print(is_palindrome("kayak"))
print(is_palindrome("Goodbye"))
