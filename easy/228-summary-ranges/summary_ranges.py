def summary_ranges(nums: list[int])->list[int]:
    start = nums[0]
    territories = []

    for i in range(len(nums) + 2):
        if start+1 == nums[i+1]:
            territories.append(nums[i])
        start = nums[i]
        print(start)

print(summary_ranges([0, 1, 2, 4, 5, 7])) #["0->2", "4->5", "7"]
print(summary_ranges([0, 2, 3, 4, 6, 8, 9])) #["0", "2->4", "6", "8->9"]
print(summary_ranges([3, 4, 5, 8, 10, 11, 12]))


