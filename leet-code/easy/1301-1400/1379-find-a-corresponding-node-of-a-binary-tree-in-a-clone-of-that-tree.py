# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#
# The cloned tree is a copy of the original tree.
#
# Return a reference to the same node in the cloned tree.
#
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to
# a node in the cloned tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode | None:
        if not original:
            return None

        if original is target:
            return cloned

        left = self.getTargetCopy(original.left, cloned.left, target)
        if left:
            return left

        return self.getTargetCopy(original.right, cloned.right, target)
