# 746. Min Cost Climbing Stairs
# Difficulty: Easy

# Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/

# top down dp approach
# base cases:
#   our base cost is either cost[0] or cost[1]
# when doing the dp, the current cost depends on either the last step or the one before it
# we'll use this and memoize
def solution(self, cost: list[int]) -> int:
    
    n = len(cost)
    memo = {}

    def dp(i):
        if i == 0 or i == 1:
            return cost[i]
        
        if i in memo:
            return memo[i]
        
        memo[i] = cost[i] + min(dp(i - 1), dp(i - 2))
        return memo[i]

    return min(dp(n-1), dp(n-2))


# bottom up version
# same approach but without explicit memoization
def optimized_sol(self, cost: list[int]) -> int:

    n = len(cost)
    prev1, prev2 = cost[0], cost[1]
    for i in range(2, n):
        cur = cost[i] + min(prev1, prev2)
        prev1 = prev2
        prev2 = cur
    return min(prev1, prev2)


def main():
    pass

if __name__ == "__main__":
    main()
