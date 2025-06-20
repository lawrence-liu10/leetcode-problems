# 105. Construct Binary Tree From Preorder And Inorder Traversal
# Difficulty: Medium

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# preorder: NLR, inorder: LNR
# I understand how to do it on paper, but how do you convert it to code
# first and last node are always root and deepest on right
# in an inorder traversal, we go all the way down the left path until we can't,
# then we go down the left path of the right child

# we'll keep going through the preorder list until it's equal to the inorder list vals
# then we go through the inorder list to build the left tree until they differ
# when they differ, we repeat with the next preorder value being the right child of the 
# left tree we just built
def solution(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    
    root = TreeNode(preorder[0])
    inorder_idx = 0
    stack = [root]

    for i in range(1, len(preorder)):
        node = TreeNode(preorder[i])

        if stack[-1].val != inorder[inorder_idx]:
            stack[-1].left = node
        else: # go right, keep going down inorder list until they differ
            while stack and stack[-1].val == inorder[inorder_idx]: 
                parent = stack.pop()
                inorder_idx += 1
            parent.right = node
        stack.append(node)
    
    return root



def main():
    pass

if __name__ == "__main__":
    main()
