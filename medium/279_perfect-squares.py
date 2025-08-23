# 279. Perfect Squares
# Difficulty: Medium

# Link: https://leetcode.com/problems/perfect-squares/

# came to korea for a study abroad, skipped a couple days
# for the brute force, I'm thinking keep the squares up to sqrt(n)
#   then do a coin change style approach to get the minimum
def solution(self, n: int) -> int:
    nums = []
    memo = {}
    min_nums = float('inf')
    for i in range(1, int(math.sqrt(n) + 1)):
        nums.append(i*i)
    
    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')

        if remaining in memo:
            return memo[remaining]
        
        min_steps = float('inf')
        for num in nums:
            if num > remaining:
                break
            result = dp(remaining - num)
            min_steps = min(min_steps, result + 1)

        memo[remaining] = min_steps
        return min_steps

    return dp(n)

def main():
    pass

if __name__ == "__main__":
    main()
