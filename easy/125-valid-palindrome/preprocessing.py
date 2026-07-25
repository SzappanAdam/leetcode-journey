def valid_palindrome(s: str)->bool:
    clean = ""
    for char in s:
        if char.isalnum():
            clean += char
    clean = clean.lower()

    for i in range(len(clean) // 2):
        if clean[i] != clean[len(clean) - 1 - i]:
            return False
    return True

print(valid_palindrome("abcdef"))
print(valid_palindrome("abcd"))
print(valid_palindrome("madam"))
print(valid_palindrome("baab"))
print(valid_palindrome("A man, a plan, a canal: Panama"))