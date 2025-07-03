# 1046. Last Stone Weight
# Difficulty: Easy

import heapq

# Link: https://leetcode.com/problems/last-stone-weight/description/

# let's define a heap
# while there's more than 1 element in the heap, we'll pop the top 2 from the heap
# and 'smash,' then add back to the heap
# we'll keep going until we reach at most 1 element, and return either 0 or the stone's weight

# we need a max heap though, but a simple workaround is to add negative values
# and negate them when popping

def solution(self, stones: list[int]) -> int:
    
    stones = [-x for x in stones]
    heapq.heapify(stones)

    while (len(stones) > 1):
        first_max = -heapq.heappop(stones)
        second_max = -heapq.heappop(stones)

        val = first_max - second_max
        if (val == 0):
            continue
        heapq.heappush(-val)
    
    if stones[0]:
        return -stones[0]
    return 0

def main():
    pass

if __name__ == "__main__":
    main()
