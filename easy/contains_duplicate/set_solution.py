#One pass
def contains_duplicate(nums: list[int])->bool:
    seen = set()

    for index in range(len(nums)):
        if nums[index] in seen:
            return True
        seen.add(nums[index])
    return False

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))