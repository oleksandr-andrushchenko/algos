# A binary tree is uni-valued if every node in the tree has the same value.
#
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return True
            if node.val != root.val:
                return False
            return dfs(node.left) and dfs(node.right)

        return dfs(root)
