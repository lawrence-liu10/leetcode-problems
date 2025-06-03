# 226. Invert Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/invert-binary-tree/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this can be done simply with recursion, base case we return none
# otherwise we swap left and right, then set the left and right child as the new 'root'
def solution(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

    if not root:
        return None

    temp = root.left
    root.left = root.right
    root.right = temp

    self.solution(root.left)
    self.solution(root.right)

    return root

def main():
    pass

if __name__ == "__main__":
    main()
