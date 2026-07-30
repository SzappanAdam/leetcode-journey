def contains_duplicate(nums: list[int], k: int)->bool:
    seen = {}

    for i in range(len(nums)):
        actual = nums[i]
        if actual in seen:
            index_difference = i - seen[actual]
            if index_difference <= k:
                return True
        seen[actual] = i
    return False

print(contains_duplicate([1, 2, 3, 1], 3))
print(contains_duplicate([1, 2, 3, 1, 2, 3], 2))
print(contains_duplicate([1, 2, 3, 1, 2, 3, 1], 3))