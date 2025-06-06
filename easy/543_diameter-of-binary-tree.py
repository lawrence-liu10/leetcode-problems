# 543. Diameter Of Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# the diameter at any node is the max of the left subtree, the right subtree, or
#   the height of the left tree + the height of the right tree + 1
# we can use this to implement a recursive solution

# if a node is null, its height is zero
# otherwise, we check the height of the left and right subtree, updating the diameter if that's larger than the current one
# at each step, we return this max diameter + 1 (accounting for the current node)
# time complexity: O(n)
# space complexity: O(n)
# time to solve: 30 min

def solution(self, root: TreeNode) -> int:
    self.diameter = 0

    def height(node: TreeNode):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)

        self.diameter = max(self.diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    height(root)
    return self.diameter


def main():
    pass

if __name__ == "__main__":
    main()
