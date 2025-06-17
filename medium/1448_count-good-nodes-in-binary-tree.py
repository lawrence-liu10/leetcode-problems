# 1448. Count Good Nodes In Binary Tree
# Difficulty: Medium

# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from collections import deque
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# for recursive dfs, I'm thinking we define the function as such
# if a node is null, return
# otherwise, we traverse the tree, returning a node and the max node seen at each point
# if the max node <= cur, add one to good nodes seen
def solution(self, root: TreeNode) -> int:
    
    good_nodes = 0
    def dfs(root, max_val):
        if not root:
            return
        nonlocal good_nodes
        if max_val <= root.val:
            good_nodes += 1
            max_val = max(max_val, root.val)

        dfs(root.right, max_val)
        dfs(root.left, max_val)
    dfs(root, -float('inf'))
    return good_nodes

# bfs solution
# when doing a bfs solution, we'll use a queue
# instead of just adding nodes, we'll also add the largest num seen with it
def bfs(self, root: TreeNode) -> int:
    
    sol = 0
    queue = deque()
    queue.append((root, -float('inf')))

    while queue:
        node, max_val = queue.popleft()

        if max_val <= node.val:
            sol += 1
            max_val = max(max_val, node.val)
        
        if node.left:
            queue.append((node.left, max_val))
        if node.right:
            queue.append((node.right, max_val))

    return sol
            

def main():
    pass

if __name__ == "__main__":
    main()
