# 572. Subtree Of Another Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/subtree-of-another-tree/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# we can define a helper function to check if two trees are the same, and then go through the tree
# if both trees have the same root, we'll check if they're the same
# there's some edge cases we have to define, a null main tree will never work,
# and a null subtree will always work
# by our implementation, we also need to explicitly compare the main tree with the subtree
# because we only compare the children
# time complexity: O(m * n), where m is the size of m
# space complexity: O(n)
# time to solve: 30 min
def solution(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)

    if not subRoot:
        return True
    if not root:
        return False

    # if sameTree(self, root, subRoot):
    #     return True

    return (self.solution(root.left, subRoot) or self.solution(root.right, subRoot))

# iterative dfs
# we'll still use a helper function in this case
# it's the same function as same tree, where if both are null, we've reached the end of both trees and they're the same
# if one is null, or values are diff they're not the same
# otherwise, we move down the tree with a manually created stack
def iterative_dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def sameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [(root, subRoot)]
        while stack:
            root_n, sub_n = stack.pop()

            if not root_n and not sub_n:
                continue
            if not root_n or not sub_n:
                return False
            if root_n.val != sub_n.val:
                return False

            stack.append((root_n.left, sub_n.left))
            stack.append((root_n.right, sub_n.right))

        return True

    stack = [root]

    while stack:
        node = stack.pop()

        if not node:
            continue
        if sameTree(node, subRoot):
            return True

        stack.append(node.left)
        stack.append(node.right)

    return False


# bfs approach would be almost exactly identical. We'd still need the helper function,
# but we'd use a deque to implement it instead of a stack
# we'd also have to explicitly define edge cases given that bfs can't handle empty nodes



def main():
    pass

if __name__ == "__main__":
    main()
