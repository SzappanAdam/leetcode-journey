def group_anagrams(strings: list[str])->list[str]:
    group = {}

    for string in strings:
        asc = ''.join(sorted(string))
        if asc not in group:
            group[asc] = [string]
        else:
            group[asc].append(string)

    return list(group.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams([""]))
print(group_anagrams(["a"]))