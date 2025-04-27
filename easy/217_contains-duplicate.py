# 217. Contains Duplicate
# Difficulty: Easy

# Link: https://leetcode.com/problems/contains-duplicate/description/

# sort and iterate, true if n == n-1
# Time: O(nlog(n)) (+ O(n) to iterate)
# Space: O(n) depending on sort (python's sort() is O(n))
def solution1(nums: list[int]) -> bool:
    
    nums.sort()
    for i in range (1, len(nums) - 1):
        if nums[i] == nums[i-1]:
            return True
    
    return False

# add to a hashset, iterate and check if key exists
# Time: O(n)
# Space: O(n)
def solution2(nums: list[int]) -> bool:

    exists = set()
    for num in nums:
        if num in exists:
            return True
        exists.add(num)

    return False


def main():
    
    nums1 = [1,2,3,1]
    nums2 = [1,2,3,4]
    nums3 = [1,1,1,3,3,4,3,2,4,2]

    #print(solution1(nums3))
    print(solution2(nums3))

if __name__ == "__main__":
    main()
