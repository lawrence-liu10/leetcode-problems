# 110. Balanced Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# going from top to bottom seems bad, we have to calculate the height of every subtree
#   which leads to a lot of repeated steps
# we need to work from the leaves up, we can do it recursively
# from the leaves, we set the height to 0, and check if subtrees are balanced

# base case, a null node, the subtree is balanced and the height is 0
# recursive step, we check if the height of the l subtree and r subtree differ by <= 1, and if the children subtrees are balanced
# if so, the current subtree will be balanced
# time complexity: O(n)
# space complexity: O(n)
# time to solve: 40 min
def solution(self, root: Optional[TreeNode]) -> bool:

    def check(node):
        if not node:
            return 0, True

        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        cur_height = 1 + max(left_height, right_height)
        is_balanced = (left_balanced and right_balanced and
                       abs(left_height - right_height) <= 1)

        return cur_height, is_balanced

    height, balanced = check(root)
    return balanced

def main():

    pass

if __name__ == "__main__":
    main()
