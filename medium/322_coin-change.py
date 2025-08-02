# 322. Coin Change
# Difficulty: Medium

# Link: https://leetcode.com/problems/coin-change/

# to do this question, lets do a dynamic programming approach
# we'll keep track of the remaining coins required to make the correct change,
# and go through each coin in coins to recursively calculate down to the target
def solution(self, coins: list[int], amount: int) -> int:
    memo = {}

    def dp(remaining):
        if remaining in memo:
            return memo[remaining]
        if remaining == 0:
            return 0
        if remaining < 0:
            return -1
        
        min_coins = float('inf')
        for coin in coins:
            sol = dp(remaining - coin)
            if sol >= 0:
                min_coins = min(min_coins, sol + 1)
        
        memo[remaining] = min_coins if min_coins != float('inf') else -1
        return memo[remaining]
    
    return dp(amount)

# for the bottom up approach, we can use a dp array up to amount (+ 1 b/c 0 index)
#   for the base case, it takes 0 coins to make change of 0
#   otherwise, for every amount we'll try every possible coin, and if a coin can fit in the amount,
#       we check if there's a better solution
def bottom_up(self, coins: list[int], amount: int) -> int:

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[amount] == float('inf'):
        return -1
    return dp[amount]


def main():
    pass

if __name__ == "__main__":
    main()
