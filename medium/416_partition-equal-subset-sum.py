# 416. Partition Equal Subset Sum
# Difficulty: Medium

# Link: https://leetcode.com/problems/partition-equal-subset-sum/description/

# first, the numbers must be even to be split evenly
# otherwise, we can loop through the array choosing to either include a number or not
#   if a sum eventually equals half the total sum, then it can be evenly split
#   we'll memoize to reduce calculations
def solution(self, nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    memo = {}

    def dp(i, remaining):
        if remaining == 0:
            return True
        if i >= len(nums) or remaining < 0:
            return False
        if (i, remaining) in memo:
            return memo[(i, remaining)]
        
        memo[(i, remaining)] = dp(i + 1, remaining - nums[i]) or dp(i + 1, remaining)
        return memo[(i, remaining)]
    
    return dp(0, target)


# for the bottom up,
#   we'll set up a dp array representing the possible sums from 0 to our target
#   we'll work backwards from the target to our current num, and 
#       check if previous sums can be calculated
#   at the end, if the target is true then it can be partitioned
def bottom_up(self, nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0]= True

    for num in nums:
        for sum in range(target, num - 1, -1):
            dp[sum] = dp[sum] or dp[sum - num]
    
    return dp[target]

def main():
    pass

if __name__ == "__main__":
    main()
