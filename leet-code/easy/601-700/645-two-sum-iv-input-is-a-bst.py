# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that
# their sum is equal to k, or false otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        seen = set()

        def dfs(node: TreeNode | None) -> bool:
            if not node:
                return False

            if k - node.val in seen:
                return True

            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
