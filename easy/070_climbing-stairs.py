# 070. Climbing Stairs
# Difficulty: Easy

# Link: https://leetcode.com/problems/climbing-stairs/description/

# we can solve with backtracking but it's extremely slow, recalculating each step
#   time limit exceeded, we need to memoize
def backtrack(self, n: int) -> int:
    
    ways = 0

    def dfs(cur):
        if cur > n:
            return
        if cur == n:
            ways += 1
            return
        
        dfs(cur + 1)
        dfs(cur + 2)
    
    return ways

# dp approach
# define base cases
#   at the last step, there's one way to get to the last step (we're there)
#   at the second to last step, there's one way to get to the last (take one step)
# now we work backwards. from the third to last step, there's two ways to get to the end, so we add
#   we continue backwards until we reach the first step
# very slow still, we can do it iteratively AND without memoizing, just keeping track of two variables
def dp_sol1(self, n: int) -> int:

    def dp(n, memo):
        if n == 0 or n == 1:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = dp(n - 1, memo) + dp(n - 2, memo)
        return memo[n]
    
    return dp(n, {})


# constant space solution, no recursion
# we start from the end and work backwards, because # ways only depends on the previous two steps
#   we can then only track the last two steps and keep moving them
def dp_sol2(self, n: int) -> int:

    if n == 0 or n == 1:
        return 1
    
    prev1, prev2 = 1, 1
    for i in range(2, n + 1):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    return prev1

def main():
    pass

if __name__ == "__main__":
    main()
