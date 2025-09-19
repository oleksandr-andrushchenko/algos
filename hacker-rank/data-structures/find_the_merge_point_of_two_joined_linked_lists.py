# Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge.
# The merge point is where both lists point to the same node, i.e. they reference the same memory location.
# It is guaranteed that the two head nodes will be different, and neither will be NULL.
# If the lists share a common node, return that node's  value.
#
# Note: After the merge point, both lists will share the same node pointers.


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    return findMergeNode_brute(head1, head2)
    return findMergeNode_two_pointers(head1, head2)


def findMergeNode_brute(head1, head2):
    head2_copy = head2
    while head1:
        head2 = head2_copy
        while head2:
            if head1 == head2:
                return head1.data
            head2 = head2.next
        head1 = head1.next

    return None


def findMergeNode_two_pointers(head1, head2):
    pt1, pt2 = head1, head2

    while pt1 != pt2:
        pt1 = pt1.next if pt1 else head2
        pt2 = pt2.next if pt2 else head1

    return pt1.data if pt1 else None


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count - 1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
