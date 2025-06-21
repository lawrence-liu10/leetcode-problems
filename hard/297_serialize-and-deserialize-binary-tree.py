# 297. Serialize And Deserialize Binary Tree
# Difficulty: Hard

# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# first idea is to do a bfs with a deque, and build a string in level order
# we'll use commas as delimiters, null for null nodes, and l/r + number
# actually we don't need l/r because they'll be filled in by nulls
def serialize(self, root):
        
    if not root:
        return "null"

    sol = []
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if not node:
                sol.append("null")
            else:
                sol.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
    
    return ",".join(sol)

# when deserializing, we do the opposite

def deserialize(self, data):
    
    tree = data.split(",")
    if tree[0] == "null":
        return None

    root = TreeNode(tree[0])
    queue = deque([root])
    i = 1
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if tree[i] != "null":
                new_node = TreeNode(tree[i])
                node.left = new_node
                queue.append(node.left)
            i += 1
            if tree[i] != "null":
                new_node = TreeNode(tree[i])
                node.right = new_node
                queue.append(node.right)
            i += 1
    return root




def main():
    pass

if __name__ == "__main__":
    main()
