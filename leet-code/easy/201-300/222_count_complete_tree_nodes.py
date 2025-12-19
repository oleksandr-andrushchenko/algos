# Given the root of a complete binary tree, return the number of the nodes in the tree.
#
# According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Design an algorithm that runs in less than O(n) time complexity.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def get_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if left_height == right_height:
            # Left subtree is perfect
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect but one level smaller
            return (1 << right_height) + self.countNodes(root.left)
