# 300. Longest Increasing Subsequence
# Difficulty: Medium

# Link: https://leetcode.com/problems/longest-increasing-subsequence/

# we'll solve using dp
#   we'll memoize our past results
#   and at each i, we'll choose to either include (add 1 to length) or skip it before continuing
#   when we reach the end of the list, return
#   the top down approach tests out of memory
def solution(self, nums: list[int]) -> int:

    memo = {}
    def dp(prev, i):
        if i == len(nums):
            return 0
        if (prev, i) in memo:
            return memo[(prev, i)]
        taken = 0
        if prev == -1 or nums[i] > nums[prev]:
            taken = 1 + dp(i, i + 1)
        not_taken = dp(prev, i + 1)
        memo[(prev, i)] = max(taken, not_taken)
        return memo[(prev, i)]
    
    return dp(-1, 0)


# checking if I could come up with the bottom up solution again
#   for each num, we take the max length before it plus one or the current max
def bottom_up(self, nums: list[int]) -> int:

    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                nums[i] = max(dp[i], nums[j] + 1)
    

    return max(dp)


def main():
    pass

if __name__ == "__main__":
    main()
