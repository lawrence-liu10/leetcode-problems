# 121. Best Time To Buy And Sell Stock
# Difficulty: Easy

# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# doing to practice dp
# for the dp approach, the max profit on any day is either
#   the previous max, or the current price minus the minimum price up to current
#       we go through updating both, and the last value holds the final max
def solution(self, prices: list[int]) -> int:
    dp = [0] * len(prices)
    min_price = prices[0]

    for i in range(1, len(prices)):
        min_price = min(prices[i], min_price)
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[-1]

# bottom up
#   keep track of the minimum price and the maximum profit and return at the end
def bottom_up(self, prices: list[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        min_price = min(prices[i], min_price)
        if prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit

def main():
    pass

if __name__ == "__main__":
    main()
