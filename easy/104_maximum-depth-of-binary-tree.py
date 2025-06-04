# 104. Maximum Depth Of Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# we can do this recursively, just travel down the left and right subtree
# base case of a null node, return 0
# otherwise, return 1 + the max of the left or right subtree
# time complexity: O(n)
# space complexity: O(n)
# time to solve: 5 min
def solution(self, root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    return 1 + max(self.solution(root.left), self.solution(root.right))

def main():
    pass

if __name__ == "__main__":
    main()
