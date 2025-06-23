# 235. Lowest Common Ancestor Of A Binary Tree
# Difficulty: Medium

# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# for the problem intuition, p and q's lowest ancestor will be the node that splits
# the paths to p and q, where they end up in different subtrees
# we traverse the tree going left if they're less than the current node, and right otherwise
def solution(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root

def main():
    pass

if __name__ == "__main__":
    main()
