def valid_palindrome(s: str)->bool:
    left = 0
    right = len(s) - 1 
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

print(valid_palindrome("abcdef"))
print(valid_palindrome("abcd"))
print(valid_palindrome("madam"))
print(valid_palindrome("baab"))
print(valid_palindrome("A man, a plan, a canal: Panama"))