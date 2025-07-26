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
        

def main():
    pass

if __name__ == "__main__":
    main()
