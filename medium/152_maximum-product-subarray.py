# 152. Maximum Product Subarray
# Difficulty: Medium

# Link: https://leetcode.com/problems/maximum-product-subarray/description/

# for the top down dp approach, we'll work our way in from the max subarray
# if a subarray has been seen before, we'll add it to the dict, then keep checking smaller subarrays
def solution(self, nums: list[int]) -> int:
    memo = {}

    def dp(start, end):
        if (start, end) in memo:
            return memo[(start, end)]
        if start == end:
            memo[(start, end)] = nums[start]
            return nums[start]
        
        product = 1
        for i in range(start, end + 1):
            product *= nums[i]
        memo[(start, end)] = max(product, dp(start, end - 1), dp(start + 1, end))
        return memo[(start, end)]

    return dp(0, len(nums) - 1)

# top down approach is too slow, we a more efficient approach
#   if we keep track of the min/max product at any i, we can handle negatives
#   we'll multiply new negatives by our minimum product to make them positive, or just update our max
# we also need to store the current max in a temp variable to properly calculate the current min
def solution(self, nums: list[int]) -> int:
    total_max = cur_max = cur_min = nums[0]
    for num in nums[1:]:
        temp_max = max(num, cur_min * num, cur_max * num)
        cur_min = min(num, cur_min * num, cur_max * num)
        cur_max = temp_max
        total_max = max(total_max, cur_max)
    return total_max



def main():
    pass

if __name__ == "__main__":
    main()
