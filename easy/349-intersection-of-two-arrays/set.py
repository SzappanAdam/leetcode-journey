def intersection_of_two_arrays(nums1: list[int], nums2: list[int])->list[int]:
    intersection = [] 

    set1 = set(nums1)
    set2 = set(nums2)

    for num in set1:
        if num in set2:
            intersection.append(num)
    return intersection
            
print(intersection_of_two_arrays([1, 2, 2, 1], [2, 2]))
print(intersection_of_two_arrays([4, 9, 5], [9, 4, 9, 8, 4]))