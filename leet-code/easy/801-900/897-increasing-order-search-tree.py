# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now
# the root of the tree, and every node has no left child and only one right child.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        stack = []
        dummy = TreeNode(0)
        curr = dummy

        while stack or root:
            # Go to leftmost node
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # Re-link nodes
            root.left = None
            curr.right = root
            curr = root

            root = root.right

        return dummy.right
