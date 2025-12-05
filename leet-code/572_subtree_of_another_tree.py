# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def isSame(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (
                    a.val == b.val
                    and isSame(a.left, b.left)
                    and isSame(a.right, b.right)
            )

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and isSame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
