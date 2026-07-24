# Two Sum

## Approach
Used a hash map to store previously seen numbers and their indices.

For each number:
1. Calculate the required complement.
2. Check if the complement was already seen.
3. If yes, return both indices.
4. Otherwise store the current number.

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)