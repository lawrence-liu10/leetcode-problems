# 973. K Closest Points To Origin
# Difficulty: Medium

import math
import heapq

# Link: https://leetcode.com/problems/k-closest-points-to-origin/description/

# let's define a helper to calculate distances to make it a little cleaner

# besides that, we'll make a heap of distances and points
# we'll also keep track of the minimum distance we push into the array
# for any new element, it must be at least that distance to append
# we pop any time the heap has over k elements
# and return at the end 
def solution(self, points: list[list[int]], k: int) -> list[list[int]]:
    
    def dist(point: list[int]):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
    
    max_heap = []
    
    for point in points:
        distance = dist(point)
        heapq.heappush(max_heap, [-distance, point])
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    sol = []
    while max_heap:
        val, point = max_heap.pop()
        sol.append(point)

    return sol
        



def main():
    pass

if __name__ == "__main__":
    main()
