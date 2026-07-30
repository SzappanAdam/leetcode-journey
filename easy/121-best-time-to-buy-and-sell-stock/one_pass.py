def best_time_to_buy_and_sell_stock(prices: list[int])->int:
    minimum = prices[0]
    maximum_profit = 0

    for price in prices:
        actual = price - minimum
        if actual > maximum_profit:
            maximum_profit = actual
        if price < minimum:
            minimum = price
    return maximum_profit

print(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
print(best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]))