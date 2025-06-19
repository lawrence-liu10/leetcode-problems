# 230. Kth Smallest Element In A BST
# Difficulty: Medium

from collections import deque
from typing import Optional
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# My first idea is to use bfs combined with a min heap
# at the end of the tree, we pop k times
# making a whole min heap is pretty inefficient though
# the time complexity is about the same as sorting an arr, but sorting has a higher space complexity
def solution(self, root: Optional[TreeNode], k: int) -> int:
    
    queue = deque([root])
    min_heap = []

    while queue:
        for _ in range(len(queue)):
            node = queue.pop()

            if not node:
                continue

            heapq.heappush(min_heap, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    for _ in range(k - 1):
        heapq.heappop(min_heap)

    return heapq.heappop(min_heap)

# it's a lot more efficient to just run an inorder traversal with recursive dfs
# LNR, we basically append from least to greatest, so we remove the need to sort
def inorder_dfs(self, root: Optional[TreeNode], k: int) -> int:

    arr = []

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)

    dfs(root)
    return arr[k]

# we can improve even further by skipping the array, which allows us to stop when
#   we reach the kth smallest element immediately
def inorder_dfs(self, root: Optional[TreeNode], k: int) -> int:

    ans = root.val

    def dfs(node):
        nonlocal ans, k

        if not node:
            return

        dfs(node.left)
        k -= 1
        if k == 0:
            ans = node.val
            return
        dfs(node.right)
    
    dfs(root)
    return ans

# iterative dfs now
# inorder traversal is a little different than pre or post order
# we need to go all the way down the left tree, first before lookig at node
def inorder_dfs(self, root: Optional[TreeNode], k: int) -> int:
    
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        k -= 1
        if k == 0:
            return cur.val
        cur = cur.right
        


        


def main():
    pass

if __name__ == "__main__":
    main()
