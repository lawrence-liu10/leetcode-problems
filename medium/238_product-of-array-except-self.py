# 238. Product Of Array Except Self
# Difficulty: Medium

# Link: https://leetcode.com/problems/product-of-array-except-self/

# brute force O(n^2), just do two loops but we can do better
# with division we could just keep track of # zeroes and a total product
# I know it has to do with product prefix and suffix arrays, but how?
# thinking done at bottom of file
# Time complexity: O(n)
# Space complexity: O(n)
def solution1(nums: list[int]) -> list[int]:

    n = len(nums)
    prefix = [0] * n
    suffix = [0] * n
    sol = [0] * n


    prefix[0] = nums[0]
    for i in range(1, n):
        prefix[i] = nums[i] * prefix[i - 1]
    
    suffix[n - 1] = nums[n - 1]
    for i in range (n - 2, -1, -1):
        suffix[i] = nums[i] * suffix[i + 1]

    sol[0] = suffix[1]
    sol[n - 1] = prefix[n - 2]
    for i in range(1, n - 1):
        sol[i] = prefix[i - 1] * suffix[i + 1]
    return sol

# can we shorten pre and suf array creation into one loop
def solution2(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [0] * n
    suffix = [0] * n
    sol = [0] * n

    pre_prod = 1
    suf_prod = 1
    for i in range(n):
        pre_prod *= nums[i]
        prefix[i] = pre_prod

        suf_prod *= nums[n - i - 1]
        suffix[n - i - 1] = suf_prod

    sol[0] = suffix[1]
    sol[n - 1] = prefix[n - 2]
    for i in range(1, n - 1):
        sol[i] = prefix[i - 1] * suffix[i + 1]
    return sol

# two passes, no extra space
# fill with left prod, then mult by right prod
def solution2(nums: list[int]) -> list[int]:
    left_prod = 1
    right_prod = 1
    n = len(nums)

    sol = [0] * n
    for i in range(n):
        sol[i] = left_prod
        left_prod *= nums[i]

    for i in range(n - 1, -1, -1):
        sol[i] *= right_prod
        right_prod *= nums[i]

    return sol



def main():
    
    nums1 = [1,2,3,4]
    print(solution2(nums1))

    nums2 = [2,3,5,4]
    print(solution2(nums2))

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


# how can we compress to one loop
# keep running products from left and right
# for suffix, we index by n - i - 1 to decrement

# for O(1) space complexity, we don't need the arrays
# need to use left and right product
# previous pre and suf array don't seem to help
# what if we lag it one behind, and keep out of bounds as one
    #[1,2,3,4] solution = [24,12,8,6]
    #lp=1, rp=1
    #lp=1, rp=4
    #lp=2, rp=12
    #lp=6, rp=24
    #[1,1,2,6]
    # [1,4,12,24] flip, [24,12,4,1] and mult we get [24,12,8,6]
    # two loops, one fills with lp, second mult by rp
