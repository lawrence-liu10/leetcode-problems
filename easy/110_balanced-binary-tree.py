# 110. Balanced Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/balanced-binary-tree/description/

from collections import deque
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

# iterative dfs approach
# we avoid the recursion stack overhead, and avoid stack overflow, so it's more efficient in general but harder to implement

# we process nodes in post order, and keep track of heights using a hash map
# we'll push nodes to the stack until we reach the leftmost leaf, then check the right child
#   after processing the subtrees, we calculate the current height and check if they're balanced
#   if there's ever an unbalanced subtree, the whole tree is unbalanced
def iterative_dfs(self, root: Optional[TreeNode]) -> bool:
    stack = []
    node = root
    last_visited = None
    heights = {} # node:height

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek = stack[-1]
            # if there's a right child and it isn't processed
            if peek.right and peek.right != last_visited:
                node = peek.right
            else:
                left_height = heights.get(peek.left, 0)
                right_height = heights.get(peek.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[peek] = 1 + max(left_height, right_height)
                last_visited = stack.pop()

    return True



# bfs approach isn't efficient because we work from the leaves up, so I'll skip it

def main():

    pass

if __name__ == "__main__":
    main()
