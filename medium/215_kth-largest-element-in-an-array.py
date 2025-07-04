# 215. Kth Largest Element In An Array
# Difficulty: Medium

# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq

# we can just negate each number, heapify, and then return the negated kth popped element
# time complexity: O(n) negation, O(n) heapify, O(klogn) heappop, so O(n + klogn)
# O(n) space for the negated list
def solution(self, nums: list[int], k: int) -> int:
    
    nums = [-x for x in nums]
    heapq.heapify(nums)
    sol = 0
    for i in range(k):
        sol = heapq.heappop(nums)
    
    return sol


def main():
    pass

if __name__ == "__main__":
    main()
