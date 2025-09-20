# Given a pointer to the root of a binary tree, print the top view of the binary tree.
#
# The tree as seen from the top the nodes, is called the top view of the tree.

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

from collections import deque


def topView(root):
    if root is None:
        return

    # Map to store first node at each horizontal distance
    hd_map = {}

    # Queue for BFS: (node, horizontal_distance)
    q = deque([(root, 0)])

    while q:
        node, hd = q.popleft()

        # Record first node at this HD
        if hd not in hd_map:
            hd_map[hd] = node.info

        # Add children with updated HD
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))

    # Print values sorted by HD
    for hd in sorted(hd_map):
        print(hd_map[hd], end=" ")


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
