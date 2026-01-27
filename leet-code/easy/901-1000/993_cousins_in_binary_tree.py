# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return
# true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
#
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
#
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        info = {}  # val -> (depth, parent)

        def dfs(node: TreeNode | None, parent: TreeNode | None, depth: int):
            if not node:
                return

            if node.val == x or node.val == y:
                info[node.val] = (depth, parent)

            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)

        dfs(root, None, 0)

        if x not in info or y not in info:
            return False

        depth_x, parent_x = info[x]
        depth_y, parent_y = info[y]

        return depth_x == depth_y and parent_x != parent_y
