# 002. Add Two Numbers
# Difficulty: Medium

# Link: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# looks like a stack question, we can add each number to a stack and then
# read them as strings, before converting them to ints and then adding
# we can then read the string backwards while making each number a node
# currently works for same length ints, need to adjust for different lengths
# did some adjustments
# there's a lot of overhead with the function calls, could probably be faster with an arithmetic based approach
# time complexity: O(n), n = total length of l1 and l2
# space complexity: O(n)
def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    stack1 = []
    stack2 = []

    while l1:
        stack1.append(str(l1.val))
        l1 = l1.next

    while l2:
        stack2.append(str(l2.val))
        l2 = l2.next

    total = str(int(''.join(reversed(stack1))) + int(''.join(reversed(stack2))))

    iter = ans = ListNode()
    for digit in reversed(total):
        iter.next = ListNode(int(digit))
        iter = iter.next

    return ans.next


def main():
    pass

if __name__ == "__main__":
    main()
