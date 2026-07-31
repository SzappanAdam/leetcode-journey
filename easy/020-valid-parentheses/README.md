# 20. Valid Parentheses

## Problem

Given a string `s` containing only the characters `(`, `)`, `[`, `]`, `{`, and `}`, determine whether the input string is valid.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket.
2. Brackets are closed in the correct order.
3. Every closing bracket has a corresponding opening bracket.

## Examples

* `"()"` → `True`
* `"()[]{}"` → `True`
* `"(]"` → `False`
* `"([)]"` → `False`
* `"{[]}"` → `True`
* `"({[]})"` → `True`

---

## Approach — Stack

### Idea

The problem follows a **Last In, First Out (LIFO)** pattern.

Whenever an opening bracket is encountered, it is added to a stack.

When a closing bracket is encountered, the most recently opened bracket must be checked first.

A dictionary is used to store the relationship between closing and opening brackets:

```text
")" → "("
"]" → "["
"}" → "{"
```

For every closing bracket:

1. Check whether the stack contains an opening bracket.
2. Compare the top of the stack with the expected opening bracket.
3. If they do not match, return `False`.
4. If they match, remove the opening bracket from the stack.

After processing the entire string, the stack must be empty for the string to be valid.

### Complexity

* **Time:** O(n)
* **Space:** O(n)

Each character is processed once.

In the worst case, the stack can contain every character in the input string, resulting in O(n) additional space.

## Key Takeaway

This problem introduces the **stack** data structure and the **LIFO (Last In, First Out)** principle.

The most recently opened bracket must always be closed first.

The problem also demonstrates how a dictionary can be used to represent relationships between values:

```text
closing bracket → opening bracket
```

The combination of a stack and dictionary provides an efficient O(n) solution.
