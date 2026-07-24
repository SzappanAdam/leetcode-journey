def TwoSum(nums: list[int], target: int)->list[int]:
    seen = {}

    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in seen:
            return [seen[complement], index]
        seen[nums[index]] = index
    
print(TwoSum([2, 7, 11, 15], 9))