# Complete the  function in the editor below. It received  parameter: a pointer to the root of a binary tree.
# It must print the values in the tree's postorder traversal as a single line of space-separated values.

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


def postOrder(root):
    info = []

    def post_order(node):
        if node is None:
            return
        post_order(node.left)
        post_order(node.right)
        info.append(node.info)

    post_order(root)

    print(" ".join(map(str, info)))


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)
