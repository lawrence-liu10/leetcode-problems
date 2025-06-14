# 100. Same Tree
# Difficulty: Easy

# Link: https://leetcode.com/problems/same-tree/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# for this question we can do an iterative stack solution
# we first add the roots
#   at each level after, we pop the nodes inside
#   if they're null, skip
#   if they're not equal, return false
# otherwise we then add children and continue
# side node, we have to check if values are equal, not the nodes
# O(n) in time and space
# 15 min to solve
def solution(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    stack = [(p, q)]
    while stack:
        p_node, q_node = stack.pop()

        if not p_node and not q_node:
            continue
        if not p_node or not q_node or p_node.val != q_node.val:
            return False

        stack.append((p_node.left, p_node.left))
        stack.append((p_node.right, p_node.right))

    return True

# recursive dfs solution
# couple of base cases, we reach the end point where both nodes are null, they're the same
# if one is null and the other isn't, they're diff
# if any value is different, they're different
# and we recursively call on the children
def solution(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# bfs solution, solve by level
# for now, I'll check the same conditions but also make 2 queues, there's probably a more efficient way though
# slightly different in this case, if both are the same we just keep checking
# when we reach the end, they're completely the same
def solution(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

    p_queue = deque(p)
    q_queue = deque(q)

    while p_queue and q_queue:
        for _ in range(len(p_queue)):
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()

            if not p_node and not q_node:
                continue

            if not p_node or not q_node:
                return False

            p_queue.append(p_node.left)
            p_queue.append(p_node.right)
            q_queue.append(q_node.left)
            q_queue.append(q_node.right)

    return True








def main():
    pass

if __name__ == "__main__":
    main()
