# 133. Clone Graph
# Difficulty: Medium

# Link: https://leetcode.com/problems/clone-graph/description/

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []



# let's solve this using dfs
# we'll keep track of nodes we've already made using a hashmap to avoid duplicates
# at each step, we'll define a node and add it to the map
# otherwise, we recursively go through the neighbors list of each until we hit the end
def solution(self, node: Optional['Node']) -> Optional['Node']:
    
    if not node:
        return None
    
    visited = {}
    
    def dfs(old):
        if old in visited:
            return visited[old]
        
        new = Node(old.val)
        visited[old] = new

        new.neighbors = [dfs(node) for node in old.neighbors]
        return new
    
    return dfs(node)


def main():
    pass

if __name__ == "__main__":
    main()
