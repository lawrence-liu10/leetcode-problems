# 104. Maximum Depth Of Binary Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# we can do this recursively, just travel down the left and right subtree
# best on balanced trees
# base case of a null node, return 0
# otherwise, return 1 + the max of the left or right subtree
# time complexity: O(n)
# space complexity: O(n)
# time to solve: 5 min
def solution(self, root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    return 1 + max(self.solution(root.left), self.solution(root.right))

# iterative dfs solution
# best on unbalanced trees
# if the current node isn't null, we increment the current val, and add its children to the stack
# if it is null, we backtrack and continue popping and appending
# there's a bug with my code, I subtract the depth by 2 at each leaf,
# let's fix this by including the depth in the stack along with the node so there's no need to keep track of the height
def iterative_dfs(self, root: Optional[TreeNode]) -> int:
    stack = [(root, 1)]
    max_val = 0
    while stack:
        node, depth = stack.pop()
        if node:
            max_val = max(depth, max_val)
            stack.append(node.left, depth + 1)
            stack.append(node.right, depth + 1)

    return max_val

# max_val = 2
# cur_val = 2
# stack = [20, null]
# node = null




# bfs solution
# best on wide trees
# we iterate by level order, processing the nodes currently in the queue
#   by adding their children, when we finish a level only then move on
# we also don't need the depth var for each node, we can just define the current level
# couple bugs to hash out, we have to check if the root is null, otherwise we go through the loop even though it isn't
# same reason we have to check the children, even if we reach a level with only leaves, we'll add null nodes so we'll go through one more loop
def bfs(self, root: Optional[TreeNode]) -> int:
    queue = deque()
    if root:
        queue.append(root)

    level = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1

    return level






def main():
    pass

if __name__ == "__main__":
    main()
