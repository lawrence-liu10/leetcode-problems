# 238. Product Of Array Except Self
# Difficulty: Medium

# Link: https://leetcode.com/problems/product-of-array-except-self/

# brute force O(n^2), just do two loops but we can do better
# with division we could just keep track of # zeroes and a total product
# I know it has to do with product prefix and suffix arrays, but how?
# thinking done at bottom of file
def solution1(nums: list[int]) -> list[int]:

    prefix = [0] * len(nums)
    prefix[0] = nums[0]
    for i in range(1, len(nums)):
        prefix[i] = nums[i] * prefix[i - 1]
    
    suffix = [0] * len(nums)
    suffix[len(nums) - 1] = nums[len(nums) - 1]
    for i in range (len(nums) - 2, -1, -1):
        suffix[i] = nums[i] * suffix[i + 1]

    sol = [0] * len(nums)
    sol[0] = suffix[1]
    sol[len(nums) - 1] = prefix[len(nums) - 2]
    for i in range(1, len(nums) - 1):
        sol[i] = prefix[i - 1] * suffix[i + 1]
    return sol

# first attempt had way too much hard coding, maybe we can trim it down


def main():
    
    nums1 = [1,2,3,4] # [24,12,8,6]
    # prefix: [1, 2, 6, 24]
    # suffix: [24, 24, 12, 4]
    print(solution1(nums1))

    nums2 = [2,3,5,4] # [60, 40, 24, 30]
    # prefix: [2, 6, 30, 120]
    # suffix: [120, 60, 20, 4]
    print(solution1(nums2))

    # pattern appears to be sol[0] = suf[1], sol[len-1] = pre[len-1], obvious
    # what's the generalization
    # sol[n] = pre[n - 1] * suf[n + 1]
    # edges are as previously defined, going out of bounds = 1


if __name__ == "__main__":
    main()

# nums = [1,2,3,4], solution = [24,12,8,6]
# prefix: [1, 2, 6, 24]
# suffix: [24, 24, 12, 4]

# nums = [2,3,5,4], solution = [60, 40, 24, 30]
# prefix: [2, 6, 30, 120]
# suffix: [120, 60, 20, 4]

# pattern appears to be sol[0] = suf[0], sol[len-1] = pre[len-1], obvious
# what's the generalization
# sol[n] = pre[n - 1] * suf[n + 1]
# edges are as previously defined, going out of bounds = 1
