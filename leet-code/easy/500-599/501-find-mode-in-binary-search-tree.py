# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
#
# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        modes = []
        current_val = None
        current_count = 0
        max_count = 0

        def inorder(node):
            nonlocal current_val, current_count, max_count, modes
            if not node:
                return

            inorder(node.left)

            # Visit node
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1

            if current_count > max_count:
                max_count = current_count
                modes = [current_val]
            elif current_count == max_count:
                modes.append(current_val)

            inorder(node.right)

        inorder(root)
        return modes
