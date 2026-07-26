def valid_anagram(s: str, t: str)->bool:
    if len(s) != len(t):
        return False
    
    count = {}

    for i in range(len(s)):
        char = s[i]
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    for j in range(len(t)):
        char = t[j]
        if char not in count:
            return False
        else:
            count[char] -= 1

    for value in count.values():
        if value < 0:
            return False
    return True

print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("aab", "abb"))
print(valid_anagram("aab", "aabb"))
print(valid_anagram("aaa", "bbb"))
print(valid_anagram("", ""))