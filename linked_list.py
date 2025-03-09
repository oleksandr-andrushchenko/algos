# 🔹 13. Linked List Manipulation

# 📌 Pattern Explanation:
# Used to solve problems involving linked lists (singly, doubly, circular).
# Important for modifications, cycle detection, and merging operations.

# 📌 Concept:
# Uses pointers (head, tail, slow/fast) to navigate linked lists.

# 📌 Popular Problems:
# Reverse a Linked List
# Detect Cycle in a Linked List
# Merge Two Sorted Linked Lists
# Find Middle of a Linked List
# Remove Nth Node from End
# Reorder List (Odd-Even List)
# Flatten a Multilevel Linked List
# Copy List with Random Pointer

# 🔹 Key Techniques in Linked Lists
# ✅ 1. Fast & Slow Pointers (Floyd’s Algorithm) → Used for detecting cycles
# ✅ 2. Reversing a Linked List → Common Amazon interview problem
# ✅ 3. Merging & Sorting Linked Lists → Useful for merging sorted lists
# ✅ 4. Deleting & Finding Middle Element → Efficient solutions using two pointers
from xml.dom.minicompat import NodeList


class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head: ListNode = None):
        self.head = head

    def append(self, value):
        if not self.head:
            self.head = value if isinstance(value, ListNode) else ListNode(value)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = value if isinstance(value, ListNode) else ListNode(value)

    def print(self):
        peaces = []

        current = self.head
        while current:
            peaces.append(str(current.value))
            # peaces.append(str(current))
            current = current.next

        if peaces:
            print(' -> '.join(peaces))
        else:
            print('<Empty>')


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(5)
linked_list.print()


# ✅ Problem 1: Reverse a Linked List
# 👉 Given the head of a singly linked list, reverse it and return the new head.

# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1

# O(N) and O(1)
def reverse_list(head):
    prev = None  # This will be the new head of the reversed list
    current = head

    while current:
        next_node = current.next  # Save next node

        # prev = 1
        # current = 2
        # next = 3

        current.next = prev  # 2 -> 1 # Reverse the pointer direction
        prev = current  # prev = 2 # Move prev forward
        current = next_node  # current = 3 # Move current forward

    return prev  # `prev` now points to the new head of the reversed list


reversed_linked_list_head = reverse_list(linked_list.head)
linked_list = LinkedList(reversed_linked_list_head)
linked_list.print()

# ✅ Problem 2: Detect Cycle in a Linked List
# 👉 Given a head node, determine if there is a cycle in the linked list.

linked_list = LinkedList()
linked_list.append(1)
node = ListNode(2)
linked_list.append(node)
linked_list.append(5)
linked_list.append(node)


def has_cycle(head):
    visited = set()

    current = head
    while current:
        if current in visited:
            return True

        visited.add(current)
        current = current.next

    return False


print(has_cycle(linked_list.head))


def has_cycle_floyds(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


print(has_cycle_floyds(linked_list.head))


# ✅ Problem 3: Merge Two Sorted Linked Lists
# 👉 Given two sorted linked lists, merge them into one sorted list.

#   l1: 1 -> 4 -> 7
#   l2: 5 -> 6 -> 7 -> 8 -> 9
#   re: 1 -> 4 -> 5 -> 6 -> 7 -> 7 -> 8 -> 9

def merge_sorted_lists(l1: LinkedList, l2: LinkedList) -> ListNode:
    dummy = ListNode()
    tail = dummy

    l1_cur, l2_cur = l1.head, l2.head

    while l1_cur and l2_cur:
        if l1_cur.value <= l2_cur.value:
            tail.next = l1_cur
            l1_cur = l1_cur.next
        else:
            tail.next = l2_cur
            l2_cur = l2_cur.next
        tail = tail.next

    tail.next = l1_cur if l1_cur else l2_cur

    return dummy.next


def merge_sorted_lists_with_extra_list(l1: LinkedList, l2: LinkedList) -> LinkedList:
    l = LinkedList()

    l1_cur, l2_cur = l1.head, l2.head

    while l1_cur and l2_cur:
        if l1_cur.value <= l2_cur.value:
            l.append(l1_cur.value)
            l1_cur = l1_cur.next
        else:
            l.append(l2_cur.value)
            l2_cur = l2_cur.next

    cur = l1_cur if l1_cur else l2_cur
    while cur:
        l.append(cur.value)
        cur = cur.next

    return l


l1 = LinkedList()
l1.append(1)
l1.append(4)
l1.append(7)

l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(7)
l2.append(8)
l2.append(9)

l = merge_sorted_lists_with_extra_list(l1, l2)
l.print()


# 🔹 Two Pointers & Fast/Slow Pointer Problems

# ✅ Problem 1: Find the Middle of a Linked List
# 👉 Given a singly linked list, return the middle node.
# 👉 If there are two middle nodes, return the second one.

# l:    1 -> 2 -> 3 -> 4 -> 5
# res:  3

def find_middle(head) -> ListNode:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

print(find_middle(l.head))


# ✅ Problem 2: Remove Nth Node from End
# 👉 Given a singly linked list, remove the N-th node from the end and return the head.

#   l:      1 -> 2 -> 3 -> 4 -> 5 -> None
#   k:      2
#   res:    1 -> 2 -> 3 -> 5 -> None

# 0 <= n <= length
# index to delete: n - k

def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    slow, fast = head, head

    # Move `fast` pointer `n` steps ahead
    for _ in range(n):
        fast = fast.next

    # If `fast` is now None, we need to remove the first node
    if not fast:
        return head.next  # Skip the first node

    # Move both pointers until `fast.next` reaches the last node
    while fast.next:
        slow = slow.next
        fast = fast.next

    # `slow` is just before the node to remove
    slow.next = slow.next.next

    return head


# 🔹 Cycle Problems

# ✅ Problem 3: Find the Start of the Cycle (If Exists)
# 👉 Given a linked list with a cycle, return the node where the cycle begins.
# 👉 If there is no cycle, return None.
from typing import Optional

l = LinkedList()
l.append(1)
l.append(2)
node = ListNode(3)
l.append(node)
l.append(4)
node2 = ListNode(5)
node2.next = node
l.append(node2)


# O(n) and O(1)
def find_cycle_start(head: ListNode) -> Optional[ListNode]:
    slow, fast = head, head

    # Step 1: Detect if there is a cycle using Floyd’s Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break  # Cycle detected

    else:
        return None  # No cycle found

    # Step 2: Find the cycle start
    slow = head  # Move slow pointer to head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # The start of the cycle

print(find_cycle_start(l.head))

# 🔹 Reversing & Partitioning

# ✅ Problem 4: Reverse Nodes in k-Group
# 👉 Given a linked list, reverse every group of k nodes.
# 👉 If there are fewer than k nodes left, leave them as is.

# l = 1 → 2 → 3 → 4 → 5
# k = 2
# output = 2 → 1 → 4 → 3 → 5

def reverse_k_group(head: ListNode, k: int) -> ListNode:
    if not head or k == 1:
        return head  # No change needed for k=1 or empty list

    dummy = ListNode(0)  # Dummy node to track new head
    dummy.next = head
    prev_group_end = dummy  # Points to the last node of the previous reversed group

    while True:
        kth_node = prev_group_end  # Start of the group
        for _ in range(k):
            kth_node = kth_node.next
            if not kth_node:
                return dummy.next  # If fewer than k nodes left, return the modified list

        group_start = prev_group_end.next
        group_end = kth_node.next  # Save next group start
        kth_node.next = None  # Temporarily break connection

        # Reverse the k nodes
        prev, curr = None, group_start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect reversed group to previous part
        prev_group_end.next = prev
        group_start.next = group_end  # Connect to the next part
        prev_group_end = group_start  # Move prev_group_end to new last node


# ✅ Problem 5: Partition Linked List Around a Value
# 👉 Given a linked list and a value x, partition it so that all nodes < x come before all nodes ≥ x, while keeping the original relative order.

# l = 5 → 1 → 4 → 2 → 3
# x = 3
# output = 1 → 2 → 5 → 4 → 3

def partition_list(head: ListNode, x: int) -> ListNode:
    smaller_head = smaller_tail = None
    greater_head = greater_tail = None
    current = head

    while current:
        next_node = current.next  # Save next node (important to avoid losing reference)
        current.next = None  # Break the link to avoid unintended loops

        if current.value < x:
            if not smaller_head:
                smaller_head = smaller_tail = current  # First node in smaller list
            else:
                smaller_tail.next = current  # Append to smaller list
                smaller_tail = current  # Update tail
        else:
            if not greater_head:
                greater_head = greater_tail = current  # First node in greater list
            else:
                greater_tail.next = current  # Append to greater list
                greater_tail = current  # Update tail

        current = next_node  # Move to next node

    # If there are no nodes smaller than x, return greater list as the new head
    if not smaller_head:
        return greater_head

    # Merge smaller and greater lists
    smaller_tail.next = greater_head

    return smaller_head  # New head of the modified list
