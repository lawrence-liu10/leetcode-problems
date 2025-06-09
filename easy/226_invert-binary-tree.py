# 226. Invert Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/invert-binary-tree/

from collections import deque
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

# revisiting, but this time going to try iterative bfs, flipping by level order
# I think the way to do it is to create a stack starting with root
# at each level, we pop the existing nodes while flipping their children, and then add the flipped children
# we actually need to use a deque because we need to pop from the left
def iterative_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    queue = deque([root])
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            if not node:
                continue

            temp = node.left
            node.left = node.right
            node.right = temp
            queue.append(node.left)
            queue.append(node.right)

    return root

# let's also try to implement iterative dfs using a stack
# while the stack isn't empty, we flip the children of the current node, and
# add them to the stack
def iterative_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if not node:
            continue

        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)

    return root





def main():
    pass

if __name__ == "__main__":
    main()
