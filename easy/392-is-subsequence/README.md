# 392. Is Subsequence

## Problem

Given two strings `s` and `t`, determine whether `s` is a subsequence of `t`.

A subsequence is formed by deleting zero or more characters from a string without changing the order of the remaining characters.

## Examples

* `s = "abc"`, `t = "ahbgdc"` → `True`
* `s = "axc"`, `t = "ahbgdc"` → `False`
* `s = "ace"`, `t = "abcdef"` → `True`
* `s = "aec"`, `t = "abcdef"` → `False`

---

## Approach — Two Pointers

### Idea

Use two pointers to iterate through both strings.

* The first pointer (`i`) tracks the current character in `s`.
* The second pointer (`j`) scans through `t`.

If the characters match, move both pointers forward.

If they do not match, only move the pointer in `t`, since we continue searching for the current character of `s`.

If the pointer in `s` reaches the end of the string, every character has been found in the correct order.

### Algorithm

1. Initialize two pointers:

   * `i = 0` for string `s`
   * `j = 0` for string `t`
2. While both pointers are within their strings:

   * If `s[i] == t[j]`, increment both pointers.
   * Otherwise, increment only `j`.
3. If `i == len(s)`, return `True`; otherwise, return `False`.

### Complexity

* **Time:** O(n + m)
* **Space:** O(1)

Where:

* `n` = length of `s`
* `m` = length of `t`

Each pointer moves only forward, and every character is visited at most once.

## Key Takeaway

This problem is a classic example of the **Two Pointers** technique.

The important observation is that the pointer in the smaller string only moves when a matching character is found, while the pointer in the larger string always moves forward.

Pattern:

```text
Compare characters
        ↓
Match?
 ┌───────────────┐
 │               │
Yes             No
 │               │
i++, j++        j++
 │               │
 └────── Repeat ─┘
```

This allows the algorithm to determine whether one string is a subsequence of another in linear time using constant extra space.
