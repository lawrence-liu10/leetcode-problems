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


# iterative dfs approach
# the diameter will pass through a node which has the max sum of left and right subtree depths
# for an iterative solution, we'll first calculate the depths of each node before pushing back to the stack
#   because we start from the leaves, we'll use those to calculate the depths going upwards
#   if the sum of l and r depths are greater than the current max, update

# less efficient in time compared to recursive, given two accesses per node
# much more space efficient, no call stack memory required
# this question seems pretty difficult for an easy
def iterative_dfs(self, root: TreeNode) -> int:
    max_diameter = 0
    stack = []
    depth = {None: 0}

    stack.append((root, False))
    while stack:
        node, seen = stack.pop()
        if not node:
            continue


        if not seen:
            # put back onto stack to be processed later
            stack.append((node, True))

            stack.append((node.right, False))
            stack.append((node.left, False))
        else:
            l_depth = depth[node.left]
            r_depth = depth[node.right]

            # update current node's depth
            depth[node] = 1 + max(l_depth, r_depth)

            # max diameter is based on edges, not nodes, so we don't add one
            max_diameter = max(max_diameter, l_depth + r_depth)

    return max_diameter



def main():
    pass

if __name__ == "__main__":
    main()
