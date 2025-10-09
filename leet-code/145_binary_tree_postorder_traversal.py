# Given the root of a binary tree, return the postorder traversal of its nodes' values.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            res.append(node.val)

        traverse(root)

        return res
