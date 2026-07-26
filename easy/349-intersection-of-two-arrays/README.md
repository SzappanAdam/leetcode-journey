# 349. Intersection of Two Arrays

## Problem

Given two integer arrays `nums1` and `nums2`, return their intersection.

Each element in the result must be unique, and the order of the result does not matter.

In other words, return the elements that appear in both arrays without duplicates.

## Examples

* `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]` → `[2]`
* `nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]` → `[4, 9]`

---

## Approach — Set

### Idea

Since the result must contain only unique elements, a `set` is a natural choice for this problem.

First, convert both input arrays into sets. This automatically removes duplicate values.

Then iterate through the first set and check whether each element also exists in the second set.

If it does, add it to the result.

Because sets do not contain duplicate values, each common element is added only once.

### Complexity

* **Time:** O(n + m)
* **Space:** O(n + m)

Where `n` is the length of `nums1` and `m` is the length of `nums2`.

Creating the two sets takes linear time, and checking membership in a set takes O(1) average time.

The additional space is O(n + m) because both input arrays are converted into sets.

## Key Takeaway

A `set` is useful when we care about **unique values** and need to perform **fast membership checks**.

This problem demonstrates how converting collections into sets can simplify an algorithm while also providing efficient lookups.
