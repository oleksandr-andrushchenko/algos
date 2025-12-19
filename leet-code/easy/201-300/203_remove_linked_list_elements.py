# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Remove nodes from the beginning that match val
        while head and head.val == val:
            head = head.next

        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next  # only move forward if we didn't delete

        return head
