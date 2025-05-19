# 033. Search In Rotated Sorted Array
# Difficulty: Medium

# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# same structure as finding the minimum
# we get the number at the middle, and check it against the target
# if nums[mid] < target, we need to move right (regular binary search)
# if it's greater, it can either be to the left OR end of right
# if nums[0] > target, we have to go right of middle, it'll be at the end somewhere
# otherwise, we keep checking to the left of the inital middle
# when it's equal to the target, return

# we actually have to flip the check, first we look at nums[0] vs target
# time to solve: 45 min
# time complexity: O(n)
# space: O(1)

def solution(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


def main():
    nums = [4,5,6,7,0,1,2]
    target = 0# 4
    print(solution(nums, target))

    nums = [4,5,6,7,0,1,2] #-1
    target = 3
    print(solution(nums, target))

    nums = [1] #-1
    target = 0
    print(solution(nums, target))


if __name__ == "__main__":
    main()
