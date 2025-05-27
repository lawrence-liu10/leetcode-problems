# 021. Merge Two Sorted Lists
# Difficulty: Easy

# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# simple, just iterate through both lists, if the first is <= 2nd, 
# make temp = head, move list forward and iterate the current list
# also need to keep track of head
# took a bit to find bug, had list2 = list1.next, but otherwise simple
# time complexity: O(n + m)
# space complexity: O(1)
# time to solve: 10 min

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    temp = ListNode()
    head = temp
    while list1 and list2:
        if list1.val <= list2.val:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    
    if list1:
        temp.next = list1
    if list2:
        temp.next = list2
    
    return head.next

def main():
    pass

if __name__ == "__main__":
    main()
