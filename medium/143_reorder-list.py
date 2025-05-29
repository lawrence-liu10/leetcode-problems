# 143. Reorder List
# Difficulty: Medium

# Link: https://leetcode.com/problems/reorder-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# current idea: put the nodes on a stack, then increment the head
# while weaving in the stack nodes, making sure to change pointers
# there's a risk of a cycle in odd length lists, need to address
# time to solve: 15 min
# time complexity: O(n)
# space complexity: O(n)
def solution(head: Optional[ListNode]) -> None:
    
    stack = []
    iter = head
    count = 0

    while iter:
        stack.append(iter)
        iter = iter.next
        count += 1

    cur = head
    for _ in range(count // 2):
        next = cur.next
        right = stack.pop()
        cur.next = right
        right.next = next
        cur = next
    
    if count % 2 == 1:
        cur.next = None
    else:
        right.next = None

    return head


def main():
    pass

if __name__ == "__main__":
    main()
