# 207. Course Schedule
# Difficulty: Medium

# Link: https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict

# it looks like a cycle detection question where we're given node edges

# we can solve it using a defaultdict to define pairs,
#   and loop through the pairs, keeping track of the processed nodes
# if we explore from a source node and see a node we've visited on our current backtrack, there's a cycle
# if we see one we've previously cleared as not having a cycle, continue
# then check from 0 to numCourses - 1 for cycles
def solution(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    
    graph = defaultdict(list)
    for dest, src in prerequisites:
        graph[src].append(dest)

    visited = [0] * numCourses
    def has_cycle(node):
        if visited[node] == 1: # current backtrack
            return True
        
        if visited[node] == 2: # previously cleared, no cycle
            return False
        
        visited[node] = 1

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        
        visited[node] = 2
        return False
    
    for course in range(numCourses):
        if has_cycle(course):
            return False
        
    return True


def main():
    pass

if __name__ == "__main__":
    main()
