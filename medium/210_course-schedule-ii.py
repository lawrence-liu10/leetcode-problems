# 210. Course Schedule II
# Difficulty: Medium

# Link: https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque
# we need to check the inbound/outbound edges from each node
# we'll order it so that the nodes in front have no inbound edges (requirements)
#   unless at some point all of the nodes have an inbound edge
# we're implementing topological sort

# we need to make the adjacency list and initialize the zero-indegree nodes,
#   then keep going through the zero nodes and adding them to our final list, while subtracting one from
#   their neighbor indegrees. if we remove numCourses nodes, there's a path
#   otherwise, we return an empty list
def solution(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    
    indeg = [0] * numCourses
    neighbors = [[] for _ in range(numCourses)]
    sol = []

    for dest, src in prerequisites:
        neighbors[src].append(dest)
        indeg[dest] += 1

    topo_sort = deque()
    for i in range(numCourses):
        if indeg[i] == 0:
            topo_sort.append(i)


    while topo_sort:
        node = topo_sort.popleft()
        sol.append(node)

        for neighbor in neighbors[node]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                topo_sort.append(neighbor)
    

    if len(sol) == numCourses:
        return sol
    return []


def main():
    pass

if __name__ == "__main__":
    main()
