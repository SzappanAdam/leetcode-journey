# 219. Contains Duplicate II

## Problem

Given an integer array `nums` and an integer `k`, determine whether there are two distinct indices `i` and `j` such that:

* `nums[i] == nums[j]`
* `abs(i - j) <= k`

Return `True` if such a pair exists, otherwise return `False`.

## Examples

* `nums = [1, 2, 3, 1]`, `k = 3` → `True`
* `nums = [1, 2, 3, 1, 2, 3]`, `k = 2` → `False`
* `nums = [1, 2, 3, 1, 2, 3, 1]`, `k = 3` → `True`

In the first example, the two `1`s are at indices `0` and `3`:

`3 - 0 = 3`

Since `3 <= k`, the result is `True`.

---

## Approach — Dictionary

### Idea

A set is not enough for this problem because we need to know not only whether a value has appeared before, but also **where it appeared most recently**.

Therefore, use a dictionary where:

```text
value → most recent index
```

While iterating through the array:

1. If the current value has already been seen, calculate the difference between the current index and its previous index.
2. If the difference is less than or equal to `k`, return `True`.
3. Update the dictionary with the current index.
4. If no valid pair is found after traversing the entire array, return `False`.

The most recent index is stored because it gives the smallest possible distance to the current occurrence.

### Complexity

* **Time:** O(n)
* **Space:** O(n)

The array is traversed once, and dictionary lookups and updates take O(1) average time.

The dictionary can contain up to `n` different values, resulting in O(n) additional space.

## Key Takeaway

This problem demonstrates how a dictionary can store more than simple membership information.

Instead of storing only:

```text
value
```

we store:

```text
value → most recent index
```

This pattern is useful whenever we need to quickly find information about a previous occurrence of a value.

It also builds on the `value → index` pattern introduced in the Two Sum problem.
