# 703. Kth Largest Element In A Stream
# Difficulty: Easy

# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


import heapq

# we can do either a heap or a bst (inorder traversal and return at k)
# let's do a heap first (max heap, we can push negative numbers to make it a 'max heap')
# heaps in python have an 'nlargest' function but that kinda feels like cheating so I won't use it

# for our main object, we'll keep the min heap, and cull our elements to k
# when adding, if it's over k elements, keep it to k
# the kth largest element will be the one at the top of the heap at any given time
class KthLargest:
    def __init__(self, k: int, nums:list[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while (len(nums) > k):
            self.heap.heappop()

    def add(self, val: int) -> int:
        self.heap.heappush(self.heap, val)
        if (len(self.heap) > self.k):
            heapq.heappop(self.heap)
        
        return self.heap[0]

def solution():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
