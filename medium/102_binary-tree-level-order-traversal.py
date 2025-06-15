# 102. Binary Tree Level Order Traversal
# Difficulty: Medium

# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/


from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# simple bfs traversal, we start with the root
# at each level, we pop the nodes that were in the queue and add their children
# we can optimize slightly by only adding non-null nodes
# for a dfs approach, we'd have to manually keep track of node depths, so it's less efficient
# time to solve: 10 min
# time complexity: O(n)
# space complexity: O(n)

def solution(self, root: Optional[TreeNode]) -> list[list[int]]:

    queue = deque([root])
    ans = []
    while queue:
        cur_level = []
        for _ in range(len(queue)):
            node = queue.popleft()

            if not node:
                continue

            queue.append(node.left)
            queue.append(node.right)

            cur_level.append(node.val)

        if cur_level:
            ans.append(cur_level)

    return ans




def main():
    pass

if __name__ == "__main__":
    main()
