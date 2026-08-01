def longest_substring_without_repeating_characters(s: str)->int:
    sub = set()
    left = 0
    right = 0
    max_length = 0

    while right < len(s) :
        right_sub = s[right]
        while right_sub in sub:
            sub.remove(s[left])
            left += 1
        sub.add(right_sub)
        right += 1
        current_length = right - left
        max_length = max(max_length, current_length)

    return max_length

print(longest_substring_without_repeating_characters("abcabcbb"))
print(longest_substring_without_repeating_characters("abba"))
print(longest_substring_without_repeating_characters("bbbbb"))
print(longest_substring_without_repeating_characters("pwwkew"))
