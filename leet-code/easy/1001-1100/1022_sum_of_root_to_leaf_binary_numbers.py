# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary
# number starting with the most significant bit.
#
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of
# these numbers.
#
# The test cases are generated so that the answer fits in a 32-bits integer.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, current: int) -> int:
            if not node:
                return 0

            current = (current << 1) | node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
