# 019. Remove Nth Node From End Of List
# Difficulty: Medium

# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# we can use two pointers which are spaced n apart, and move the fast pointer to the end
# then we skip the node after the slow pointer
# we need to start at one before the head, otherwise the slow pointer will be one ahead

def solution(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next


def main():
    pass

if __name__ == "__main__":
    main()
