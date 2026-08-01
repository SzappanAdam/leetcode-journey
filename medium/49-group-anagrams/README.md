# 49. Group Anagrams

## Problem

Given an array of strings, group the anagrams together.

An anagram is a word formed by rearranging the letters of another word, using all the original letters exactly once.

The order of the output does not matter.

## Examples

Input:

```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

Output:

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## Approach — Hash Map + Sorting

### Idea

Two words are anagrams if their characters are the same after sorting.

For example:

```text
eat → aet
tea → aet
ate → aet
```

Since all anagrams produce the same sorted representation, the sorted string can be used as a dictionary key.

The dictionary stores:

* key → sorted version of the word
* value → list of words belonging to that anagram group

Example:

```text
"aet" → ["eat", "tea", "ate"]
"ant" → ["tan", "nat"]
"abt" → ["bat"]
```

### Algorithm

1. Create an empty dictionary.
2. Iterate through every word.
3. Sort the characters of the word.
4. Join the sorted characters into a string to create a key.
5. Add the original word to the corresponding group.
6. Return all dictionary values as a list.

---

## Complexity

Let:

* `n` = number of strings
* `k` = maximum length of a string

### Time Complexity

* Sorting each string takes `O(k log k)`.
* We do this for every string.

Total:

```text
O(n * k log k)
```

### Space Complexity

```text
O(n * k)
```

The dictionary stores all grouped strings.

---

## Key Takeaway

This problem demonstrates how choosing the right representation can simplify a problem.

Instead of comparing every pair of words, we transform each word into a common identifier.

Pattern:

```text
Original word
      ↓
Normalize representation
      ↓
Use as dictionary key
      ↓
Group matching values
```

This combination of hashing and normalization is a common technique used in many real-world data processing problems.
