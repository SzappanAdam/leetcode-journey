def summary_ranges(nums: list[int])->list[str]:
    if not nums:
        return []

    start = nums[0]
    territories = []

    for i in range(len(nums)):
        end_of_range = nums[i] == nums[-1] or nums[i] + 1 != nums[i + 1]
        if end_of_range:
            if start == nums[i]:
                territories.append(str(start))
            else:
                territories.append(f"{start}->{nums[i]}")
            if i != len(nums) - 1:
                start = nums[i + 1]
    return territories

print(summary_ranges([0, 1, 2, 4, 5, 7]))
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))
print(summary_ranges([3, 4, 5, 8, 10, 11, 12]))
print(summary_ranges([7]))
print(summary_ranges([1, 2]))
print(summary_ranges([]))