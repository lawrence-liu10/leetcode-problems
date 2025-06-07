# 100. Same Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/same-tree/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# for this question we can do an iterative solution
# we first add the roots
#   at each level after, we pop the nodes inside
#   if they're null, skip
#   if they're not equal, return false
# otherwise we then add children and continue
# side node, we have to check if values are equal, not the nodes
# O(n) in time and space
# 15 min to solve
def solution(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    stack = [(p, q)]
    while stack:
        p_node, q_node = stack.pop()

        if not p_node and not q_node:
            continue
        if not p_node or not q_node or p_node.val != q_node.val:
            return False

        stack.append((p_node.left, p_node.left))
        stack.append((p_node.right, p_node.right))

    return True






def main():
    pass

if __name__ == "__main__":
    main()
