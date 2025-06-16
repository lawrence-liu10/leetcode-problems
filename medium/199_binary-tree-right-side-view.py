# 199. Binary Tree Right Side View
# Difficulty: Medium

# Link: https://leetcode.com/problems/binary-tree-right-side-view/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The intuitive approach for me is using bfs
# we do a level order traversal, and the last pop at each level is the 'rightmost' node
# we store a list of these and return
def solution(self, root: Optional[TreeNode]) -> list[int]:
    
    queue = deque([root])
    sol = []
    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()

            if not node:
                continue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if i == n - 1: # level's rightmost node
                sol.append(node.val)
    
    return sol


# recursive dfs solution
# base case: if a node is null, backtrack
# otherwise, we traverse the tree in a node, right, left fashion
# this allows us to always hit the right nodes first, only going left if there's none right
# have to redefine max_depth as nonlocal in the function because it's out of its scope

def recursive_dfs(self, root: Optional[TreeNode]) -> list[int]:
    
    sol = []
    max_depth = -1

    def dfs(node, depth):
        nonlocal max_depth
        if not node:
            return
        if depth > max_depth:
            sol.append(node.val)
            max_depth += 1
        
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    
    dfs(root, 0)
    return sol

        

def main():
    pass

if __name__ == "__main__":
    main()
