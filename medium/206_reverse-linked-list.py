# 206. Reverse Linked List
# Difficulty: Medium

# Link: https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# pretty simple, 4 steps, need a prev pointer and a cur pointer
# at the end, prev holds the new head
# time complexity: O(n)
# space complexity: O(1)
# time to solve: 5 min
def solution(head: Optional[ListNode]) -> Optional[ListNode]:

    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    return prev

def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

def main():
    head = [1,2,3,4,5]#[5,4,3,2,1]
    ll = create_linked_list(head)
    print_linked_list(solution(ll))

    head = [1,2]#[2,1]
    ll = create_linked_list(head)
    print_linked_list(solution(ll))

    head = []#[]
    ll = create_linked_list(head)
    print_linked_list(solution(ll))

if __name__ == "__main__":
    main()
