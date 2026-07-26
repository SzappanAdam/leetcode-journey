# 125. Valid Palindrome

## Problem

Given a string, determine whether it is a palindrome, considering only alphanumeric characters and ignoring case.

## Examples

* `"A man, a plan, a canal: Panama"` → `True`
* `"race a car"` → `False`
* `" "` → `True`

---

## Approach 1 — Preprocessing

### Idea

First create a cleaned version of the string by removing all non-alphanumeric characters and converting the remaining characters to lowercase.

Then compare characters from the two ends toward the center.

### Complexity

* **Time:** O(n)
* **Space:** O(n)

The additional space comes from creating the cleaned string.

---

## Approach 2 — Two Pointers

### Idea

Instead of creating a new cleaned string, use two pointers:

* `left` starts at the beginning of the string.
* `right` starts at the end of the string.

The pointers move toward each other.

If a pointer encounters a non-alphanumeric character, that character is skipped because it does not matter for the palindrome check.

When both pointers point to alphanumeric characters, compare them:

* If they are different, the string is not a palindrome.
* If they are equal, move both pointers toward the center.

The process continues until the two pointers meet or cross.

### Complexity

* **Time:** O(n)
* **Space:** O(1)

Unlike the preprocessing approach, this solution does not create another string, so it uses constant extra space.

---

## Comparison

| Approach      | Time | Space | Main Idea                                |
| ------------- | ---: | ----: | ---------------------------------------- |
| Preprocessing | O(n) |  O(n) | Clean the string first                   |
| Two Pointers  | O(n) |  O(1) | Check the original string from both ends |

### Key Takeaway

The two-pointer approach improves the space complexity from **O(n)** to **O(1)** while keeping the same **O(n)** time complexity.

This is a useful example of optimizing an existing solution without changing its overall time complexity.
