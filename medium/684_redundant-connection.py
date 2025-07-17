# 684. Redundant Connection
# Difficulty: Medium

# Link: https://leetcode.com/problems/redundant-connection/description/

# we can do this simply with union find
#   we'll go through each node and set it to point to its root parent (path compression)
# this makes a shallow tree which makes it easy to process each node
# afterwards, we'll go through the reversed edges list and check if they have the same root node
# if they don't, create the parent connection
# if so, they were already connected so remove that edge
def solution(self, edges: list[list[int]]) -> list[int]:
    
    parent = [i for i in range(len(edges) + 1)] # 1 to n
    nodes = len(edges)
    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node
    
    for a,b in edges:
        root_a = find(a)
        root_b = find(b)
        if root_a == root_b:
            return [a, b]
        parent[root_b] = root_a



def main():
    pass

if __name__ == "__main__":
    main()
