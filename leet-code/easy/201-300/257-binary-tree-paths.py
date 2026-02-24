# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if not node:
                return
            # Append current node value to the path
            path.append(str(node.val))

            # If it's a leaf, join the path and add to results
            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                # Continue DFS on children
                dfs(node.left, path, result)
                dfs(node.right, path, result)

            # Backtrack
            path.pop()

        result = []
        dfs(root, [], result)
        return result
