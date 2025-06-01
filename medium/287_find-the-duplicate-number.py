# 287. Find The Duplicate Number
# Difficulty: Medium

# Link: https://leetcode.com/problems/find-the-duplicate-number/

# a duplicate must appear by pigeonhole principle
# we have to do it in constant extra space, otherwise a set would be a simple solution
# we would also be able to sort if we could modify the array
# a brute force solution would just be a double for loop, but can we do better
# I looked up a solution after 30 minutes, I don't think I would've ever got the linked list cycle solution
# time complexity: O(n)
# space complexity: O(1)
# time to solve: 40 min
def solution(nums: list[int]) -> int:
    fast = nums[nums[0]]
    slow = nums[0]
    while slow != fast:
        fast = nums[nums[fast]]
        slow = nums[slow]

    locate_cycle_start = 0
    while locate_cycle_start != slow:
        locate_cycle_start = nums[locate_cycle_start]
        slow = nums[slow]

    return slow

def main():
    nums = [1,3,4,2,2]#2
    print(solution(nums))

    nums = [3,1,3,4,2]#3
    print(solution(nums))


    nums = [3,3,3,3,3]#3
    print(solution(nums))

if __name__ == "__main__":
    main()
