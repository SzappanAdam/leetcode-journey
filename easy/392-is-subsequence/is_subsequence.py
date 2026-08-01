def is_subsequence(s: str, t: str)->bool:
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else: 
            j += 1

    return i == len(s)

print(is_subsequence("abc", "ahbgdc"))
print(is_subsequence("axc", "ahbgdc"))
print(is_subsequence("ace", "abcdef"))
print(is_subsequence("aec", "abcdef"))