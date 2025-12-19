# Given the root of a binary tree, return the sum of every tree node's tilt.
#
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right
# subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0.
# The rule is similar if the node does not have a right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode | None) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # tilt of current node
            self.total_tilt += abs(left_sum - right_sum)

            # return sum of subtree including this node
            return left_sum + right_sum + node.val

        dfs(root)
        return self.total_tilt
