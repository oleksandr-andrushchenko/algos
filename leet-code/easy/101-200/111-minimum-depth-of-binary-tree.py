# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        if not node.left:
            return 1 + self.minDepth(node.right)
        if not node.right:
            return 1 + self.minDepth(node.left)

        return 1 + min(self.minDepth(node.left), self.minDepth(node.right))
