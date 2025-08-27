# 413. Arithmetic Slices
# Difficulty: Medium

# Link: https://leetcode.com/problems/arithmetic-slices/description/

# for this question, we can use dp
#   dp[i] represents the number of arithmetic slices ending at i
#   when we extend a sequence, we get its current length + 1 new slices
#       from i, we get a new slice of length 3, 4, ..., to the end of the current sequence
def solution(self, nums: list[int]) -> int:
    dp = [0] * len(nums)
    sol = 0

    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
            sol += dp[i]
    
    return sol

def main():
    pass

if __name__ == "__main__":
    main()
