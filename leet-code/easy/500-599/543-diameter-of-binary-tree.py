# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.diameter = 0

        def depth(node: TreeNode | None) -> int:
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # Update the diameter at this node
            self.diameter = max(self.diameter, left_depth + right_depth)

            # Return the depth of this subtree
            return 1 + max(left_depth, right_depth)

        depth(root)
        return self.diameter
