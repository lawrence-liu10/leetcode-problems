# 098. Validate Binary Search Tree
# Difficulty: Medium

from collections import deque
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Link: https://leetcode.com/problems/validate-binary-search-tree/description/

# let's start with bfs solution
# just do level order traversal and keep track of max/min val
# we know that the child nodes will strictly be less/greater, so no need to call min/max
def solution(self, root: Optional[TreeNode]) -> bool:
    
    queue = deque()
    queue.append(root, -float('inf'), float('inf'))

    while queue:
        for _ in range(len(queue)):
            node, cur_min, cur_max = queue.popleft()

            # if node val is too small/big, it's false
            if node.val <= cur_min or node.val >= cur_max:
                return False

            # update min on right subtree
            if node.right:
                queue.append((node.right, node.val, cur_max))
            
            # update max on left subtree
            if node.left:
                queue.append((node.left, cur_min, node.val))
    
    return True

# dfs solution
# base case: null node, we reached the bottom successfully
# otherwise go down left side passing the node val as the max (everything must be smaller)
# and same for right side
def recursive_dfs(self, root: Optional[TreeNode]) -> bool:

    def dfs(node, min_val, max_val) -> bool:
        
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False

        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, -float('inf'), float('inf'))


def main():
    pass

if __name__ == "__main__":
    main()
