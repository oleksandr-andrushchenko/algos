# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        def merge(root, node1, node2):
            if not node1 and not node2:
                return
            elif node1 and not node2:
                root.next = ListNode(node1.val)
                merge(root.next, node1.next, node2)
            elif node2 and not node1:
                root.next = ListNode(node2.val)
                merge(root.next, node1, node2.next)
            elif node1.val <= node2.val:
                root.next = ListNode(node1.val)
                merge(root.next, node1.next, node2)
            else:
                root.next = ListNode(node2.val)
                merge(root.next, node1, node2.next)

        merge(dummy, list1, list2)

        return dummy.next
