# You are given a pointer to the root of a binary search tree and values to be inserted into the tree.
# Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree.
# You just have to complete the function.

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return

        current = self.root

        while True:
            if val > current.info:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break
            elif val < current.info:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break
            else:
                break


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
