# 704. Binary Search

## Problem

Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array.

If `target` is not present, return `-1`.

The array is sorted in ascending order.

## Examples

* `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9` → `4`
* `nums = [-1, 0, 3, 5, 9, 12]`, `target = 0` → `1`
* `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2` → `-1`

---

## Approach — Binary Search

### Idea

Because the array is sorted, we do not need to check every element individually.

The algorithm keeps track of the current search range using two pointers:

* `left` — the first index in the current search range
* `right` — the last index in the current search range

The middle index is calculated using:

```text
mid = (left + right) // 2
```

Then the middle value is compared with the target:

* If `nums[mid] == target`, return `mid`.
* If `target < nums[mid]`, the target can only be on the left side, so move `right`.
* If `target > nums[mid]`, the target can only be on the right side, so move `left`.

Each iteration eliminates approximately half of the remaining search space.

If `left` becomes greater than `right`, the target does not exist in the array, so return `-1`.

### Complexity

* **Time:** O(log n)
* **Space:** O(1)

The search space is divided in half after each iteration, resulting in logarithmic time complexity.

Only a few variables are used regardless of the input size, so the algorithm requires constant extra space.

## Key Takeaway

Binary Search is highly efficient when working with **sorted data**.

Instead of checking every element, the algorithm repeatedly examines the middle element and eliminates half of the remaining search space.

The key pattern is:

```text
sorted data
    ↓
check middle
    ↓
discard half
    ↓
repeat
```

This reduces the search complexity from O(n) with a linear search to O(log n) with Binary Search.
