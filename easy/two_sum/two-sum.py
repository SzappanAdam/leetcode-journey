#Brute Force
def two_sum(nums: list[int], target: int)->list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

print(two_sum([2, 7, 11, 15], 9))

#One pass
def TwoSum(nums: list[int], target: int)->list[int]:
    seen = {}

    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in seen:
            return [seen[complement], index]
        seen[nums[index]] = index
    
print(TwoSum([2, 7, 11, 15], 9))