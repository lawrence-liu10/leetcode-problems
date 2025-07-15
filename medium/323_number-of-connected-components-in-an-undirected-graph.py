# 323. Number Of Connected Components In An Undirected Graph
# Difficulty: Medium

# Link: https://neetcode.io/solutions/number-of-connected-components-in-an-undirected-graph

from collections import defaultdict

# we can solve this with a dfs using a visited set
#   we start from 0 and follow all outbound edges, adding them to our visited arr
#   each time we start dfs from a non-visited node, we add one to our count
def solution(self, n: int, edges: list[list[int]]) -> int:
    
    graph = defaultdict(list)
    visited = set()
    count = 0

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(cur_node):
        if cur_node in visited:
            return
        visited.add(cur_node)
        for neighbor in graph[cur_node]:
            dfs(neighbor)

    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    return count


def main():
    pass

if __name__ == "__main__":
    main()
