# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with
# a value in the inclusive range [low, high].

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0

        # If current node's value is less than low, ignore left subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        # If current node's value is greater than high, ignore right subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        # Current node is within range, include its value and recurse both sides
        return (
                root.val +
                self.rangeSumBST(root.left, low, high) +
                self.rangeSumBST(root.right, low, high)
        )
