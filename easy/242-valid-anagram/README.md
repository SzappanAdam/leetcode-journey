# 242. Valid Anagram

## Problem

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams if they contain the same characters with the same frequencies, regardless of their order.

## Examples

* `"anagram"` and `"nagaram"` → `True`
* `"rat"` and `"car"` → `False`
* `"aab"` and `"aabb"` → `False`
* `""` and `""` → `True`

---

## Approach — Character Frequency Dictionary

### Idea

The order of the characters does not matter. What matters is how many times each character appears.

First, check whether the two strings have the same length. If their lengths differ, they cannot be anagrams.

Then, create a dictionary that stores each character from `s` together with its frequency.

Next, iterate through `t` and decrease the corresponding frequency for each character.

If a character does not exist in the dictionary, the strings cannot be anagrams.

Finally, check the remaining frequencies. If any value is negative, `t` contains a character more times than `s`, so the strings are not anagrams.

If no invalid condition was found, the strings are anagrams.

### Complexity

* **Time:** O(n)
* **Space:** O(k)

Where `n` is the length of the input strings and `k` is the number of distinct characters.

For a fixed character set, `k` is bounded by a constant, so the practical auxiliary space can be considered O(1).

## Key Takeaway

Character frequency counting is useful whenever the order of elements does not matter, but their occurrences do.

This problem demonstrates how a dictionary can be used to efficiently track and compare frequencies.
