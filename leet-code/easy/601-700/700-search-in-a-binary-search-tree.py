# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
# If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST2(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        node = root
        while node:
            if node.val == val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None
