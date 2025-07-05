# 621. Task Scheduler
# Difficulty: Medium

# Link: https://leetcode.com/problems/task-scheduler/description/

import heapq
from collections import Counter
# my initial thought is this
# let's make 2 arrays, one to keep track of occurrences
#   and the other to track currently processing letters
# at each step, we want to take the largest number and process it

# we can actually use a heap to get the max at each step, instead of looping
#   through the occ array at each step
# we can also use a deque to hold our items until they're ready again,
# then push them back into the heap
# we actually don't need to keep track of letters at all, let's get rid of that
def solution(self, tasks: list[str], n: int) -> int:
    
    counts = Counter(tasks)
    max_heap = [-x for x in counts.values()]
    heapq.heapify(max_heap)

    queue = []
    steps = 0
    while max_heap or queue:

        steps += 1
        if max_heap:
            count = heapq.heappop(max_heap) + 1
            if count != 0:
                queue.append([count, steps + n])
        
        if queue and queue[0][1] == steps:
            heapq.heappush(max_heap, queue.pop(0)[0])
    
    return steps


def main():
    pass

if __name__ == "__main__":
    main()
