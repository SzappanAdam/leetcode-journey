# 3. Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within a string.

## Examples

Input:

```python
s = "abcabcbb"
```

Output:

```python
3
```

Explanation:

The longest substring without repeating characters is `"abc"`.

---

Input:

```python
s = "bbbbb"
```

Output:

```python
1
```

Explanation:

The longest substring is `"b"`.

---

Input:

```python
s = "pwwkew"
```

Output:

```python
3
```

Explanation:

The longest substring is `"wke"`.

---

## Approach — Sliding Window + Hash Set

### Idea

Maintain a sliding window that always contains unique characters.

Use two pointers:

* `left` — beginning of the current window
* `right` — end of the current window

A `set` stores all characters currently inside the window.

For each new character:

* If it is **not** in the set, expand the window.
* If it **already exists**, shrink the window from the left until the duplicate is removed.
* Update the maximum window length after each expansion.

---

## Algorithm

1. Create an empty set.
2. Initialize two pointers:

   * `left = 0`
   * `right = 0`
3. While `right` is inside the string:

   * If the current character already exists in the set:

     * Remove characters from the left side of the window until the duplicate disappears.
   * Add the current character to the set.
   * Move `right` one position forward.
   * Calculate the current window length.
   * Update the maximum length if necessary.
4. Return the maximum length found.

---

## Complexity

### Time Complexity

```text
O(n)
```

Each character enters and leaves the sliding window at most once.

### Space Complexity

```text
O(min(n, m))
```

Where:

* `n` = length of the string
* `m` = size of the character set

The set stores only the unique characters currently inside the sliding window.

---

## Key Takeaway

This problem introduces the **Sliding Window** technique.

Instead of restarting whenever a duplicate is found, the algorithm dynamically adjusts the current window by moving the left pointer only as much as necessary.

Pattern:

```text
Expand window
      │
      ▼
Duplicate found?
      │
   ┌──┴──┐
   │     │
  No    Yes
   │     │
Move    Shrink window
right   from the left
   │     │
   └──┬──┘
      ▼
Update maximum length
      │
      ▼
Continue
```

Sliding Window is one of the most important techniques for solving linear-time substring and subarray problems.
