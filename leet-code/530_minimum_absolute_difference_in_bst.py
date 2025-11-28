# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
# different nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_diff = None
        self.prev = None

    def getMinimumDifference(self, root: TreeNode | None) -> int:
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            # If we have seen a previous value, update the min difference
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)

            # Update previous value
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return int(self.min_diff)
