# 261. Graph Valid Tree
# Difficulty: Medium

# Link: https://neetcode.io/problems/valid-tree

from collections import defaultdict
from collections import deque

# a valid tree is connected, and has no cycles
# given that it has no cycles, there must be n - 1 edges (each node after the first adds 1 edge)
# afterwards, we just traverse the tree with a visited set and check if the # of visited nodes = n
def solution(self, n: int, edges: list[list[int]]) -> bool:
    if len(edges) > n - 1:
        return False
    
    visited = set()
    queue = deque()
    queue.append(0)

    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return len(visited) == n

def main():
    pass

if __name__ == "__main__":
    main()
