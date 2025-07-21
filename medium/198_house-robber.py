# 198. House Robber
# Difficulty: Medium

# Link: https://leetcode.com/problems/house-robber/description/

# dp question
# need to pick non-adjacent indices with the highest numbers
# at each step, we calc the current max val as either the 
#   current step AND the one two before, or JUST the one before (b/c of adjacency rule)
def solution(self, nums: list[int]) -> int:
    
    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i < 0:
            return 0
        if i == 0:
            return nums[0]
        
        memo[i] = max(dp(i - 2) + nums[i], dp(i - 1))
        return memo[i]
    
    return dp(len(nums) - 1)

# we don't actually need to keep track of all of the totals, just the previous 2
# bottom up approach
def bottom_up(self, nums: list[int]) -> int:

    prev2, prev1 = 0, 0
    for num in nums:
        cur = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = cur
    return prev1



def main():
    pass

if __name__ == "__main__":
    main()
