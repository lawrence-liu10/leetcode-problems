# 138. Copy List With Random Pointer
# Difficulty: Medium

# Link: https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# copying the linked list is simple, one pass to copy the list and all next pointers
# how can we set the random pointers quickly?
# can we use a stack or hashmap?
# if we use a hashmap, we can add the original as a key and the new one as a value
# any time a random points to the key, we set it to point to the value
# let's try implementing that for now
# this works but it's very slow, future me should revisit and improve
# time complexity: O(n)
# space complexity: O(n)
# time to solve: 20 min
def solution(head: 'Optional[Node]') -> 'Optional[Node]':

    if not head:
        return None

    new_list_iter = new_head = Node(head.val, head.next)
    hsm = {}
    hsm[head] = new_head

    iter = head
    while iter and iter.next:
        new_list_iter.next = Node(iter.next.val, iter.next.next)
        iter = iter.next
        new_list_iter = new_list_iter.next
        hsm[iter] = new_list_iter

    while head:
        to_point = head.random
        new_receiver = hsm.get(to_point)
        hsm.get(head).random = new_receiver
        head = head.next

    return new_head




def main():
    pass

if __name__ == "__main__":
    main()
