# 121. Best Time to Buy and Sell Stock

## Problem

You are given an array `prices` where `prices[i]` represents the price of a stock on the `i`-th day.

You may choose one day to buy the stock and a different day in the future to sell it.

The goal is to determine the maximum profit that can be achieved.

If no profitable transaction is possible, return `0`.

## Examples

* `[7, 1, 5, 3, 6, 4]` → `5`
* `[7, 6, 4, 3, 1]` → `0`

For the first example, buying at `1` and selling at `6` produces the maximum profit:

`6 - 1 = 5`

---

## Approach — One Pass

### Idea

The main observation is that we do not need to compare every possible pair of buying and selling days.

While traversing the array, keep track of two values:

* the lowest price seen so far
* the maximum profit found so far

For each price, calculate the profit that would be possible if the stock were sold on that day using the lowest price seen previously.

If this profit is greater than the current maximum profit, update it.

If the current price is lower than the stored minimum price, update the minimum.

This allows the problem to be solved in a single pass through the array.

### Complexity

* **Time:** O(n)
* **Space:** O(1)

The array is traversed only once, and only two variables are needed to store the current minimum price and maximum profit.

## Key Takeaway

Not every problem requires storing all previous values.

Sometimes it is enough to keep track of the **most important information discovered so far**.

In this problem, that information is the lowest buying price and the best profit found so far.
