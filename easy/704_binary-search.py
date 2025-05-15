# 704. Binary Search
# Difficulty: Easy

# Link: https://leetcode.com/problems/binary-search/description/

# simple and classic, just implement binary search
# if nums[middle] < target, shift to right half of the arr, vice versa
# if equal, return middle, else if l > r, return -1

# time to solve: 5 min
# time complexity: O(log(n))
# space complexity: O(n)

def solution(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

def main():
    nums = [-1,0,3,5,9,12]
    target = 9 #4
    print(solution(nums, target))

    nums = [-1,0,3,5,9,12]
    target = 2 #-1
    print(solution(nums, target))



if __name__ == "__main__":
    main()
