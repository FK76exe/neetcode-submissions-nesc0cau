class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_day = 0
        sell_day = None
        # window should be size 1
        for i, price in enumerate(prices):
            # if we have a new lowest buy price,
            # we must have a new sell date too
            if price < prices[buy_day]:
                buy_day = i
                sell_day = None
            # if we have a new highest sell price or don't have a sell date,
            # set the sell day and compare profit with maxProfit
            if not sell_day:
                sell_day = i

            profit = price - prices[buy_day]
            if profit > max_profit:
                sell_day = i
                max_profit = profit
            print(price, buy_day, sell_day)
        return max(max_profit, 0)
        