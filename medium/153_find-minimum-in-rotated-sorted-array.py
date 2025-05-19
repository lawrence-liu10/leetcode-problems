# 153. Find Minimum In Rotated Sorted Array
# Difficulty: Medium

# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# I think we can do two cases:
# first we check if arr[-1] <= arr[0] to see if any rotation happened
# if one didn't, just return arr[0]
# otherwise, we can just binary search, checking if the # at mid is > the # at r
# if it is, split to the right and keep checking
# otherwise we split to the left
# when l == r, we found the minimum
def solution(nums: list[int]) -> int:

    # if nums[0] <= nums[-1]:
    #     return nums[0]

    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2

        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    return nums[l]

def main():
    pass

if __name__ == "__main__":
    main()
