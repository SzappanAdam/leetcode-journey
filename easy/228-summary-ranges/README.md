# 228. Summary Ranges

## Problem

Given a **sorted** array of **unique integers**, return the smallest sorted list of ranges that covers every number exactly once.

Each range should be formatted as:

* `"a->b"` if the range contains multiple consecutive numbers.
* `"a"` if the range contains only a single number.

---

## Examples

### Example 1

```python
nums = [0, 1, 2, 4, 5, 7]
```

Output:

```python
["0->2", "4->5", "7"]
```

---

### Example 2

```python
nums = [0, 2, 3, 4, 6, 8, 9]
```

Output:

```python
["0", "2->4", "6", "8->9"]
```

---

## Approach

The array is already sorted and contains unique values, so we can scan it once from left to right.

We keep track of the **start** of the current range.

For every element we determine whether the current range ends:

* we reached the last element of the array, or
* the next number is **not** consecutive.

When a range ends:

* if the start and end are the same number, store a single value (`"7"`);
* otherwise, store the range (`"5->7"`).

Then begin tracking the next range.

---

## Algorithm

1. Return an empty list if the input is empty.
2. Store the first number as the start of the current range.
3. Traverse the array once.
4. Detect whether the current range ends.
5. Save either:

   * a single number, or
   * a range.
6. Start a new range if there are remaining elements.
7. Return the completed list.

---

## Complexity

### Time Complexity

```text
O(n)
```

Each element is visited exactly once.

### Space Complexity

```text
O(1)
```

Ignoring the output list, the algorithm only uses a few variables.

---

## Key Takeaway

This problem is an excellent exercise in:

* array traversal,
* handling edge cases,
* detecting consecutive sequences,
* writing clean and readable conditional logic.

A particularly useful refactoring is introducing a descriptive boolean variable such as `end_of_range`, which makes the intent of the algorithm much easier to understand.
