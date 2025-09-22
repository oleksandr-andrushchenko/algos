# For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering requirements:
#
# The  value of every node in a node's left subtree is less than the data value of that node.
# The  value of every node in a node's right subtree is greater than the data value of that node.
# Given the root node of a binary tree, can you determine if it's also a binary search tree?
#
# Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree.
# It must return a boolean denoting whether or not the binary tree is a binary search tree.
# You may have to write one or more helper functions to complete this challenge.

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def newNode():
    temp = node(-1)
    temp.left = None
    temp.right = None
    return (temp)


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(node, min_v=float("-inf"), max_v=float("inf")):
    if not node:
        return True

    if not (min_v < node.data < max_v):
        return False

    return (check_binary_search_tree_(node.left, min_v, node.data)
            and check_binary_search_tree_(node.right, node.data, max_v))


ht = int(input())
cnt = 0
values = map(int, input().split(' '))
values = list(values)
root = newNode()


def inorder(root, ht):
    global cnt
    global values
    if cnt == len(values):
        return
    else:
        if (ht > 0):
            root.left = newNode()
            inorder(root.left, ht - 1)
        root.data = values[cnt]
        cnt += 1
        if (ht > 0):
            root.right = newNode()
            inorder(root.right, ht - 1)


inorder(root, ht)
if (check_binary_search_tree_(root)):
    print("Yes")
else:
    print("No")
