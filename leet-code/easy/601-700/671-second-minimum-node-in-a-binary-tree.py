# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
# has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among
# its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        if not root:
            return -1

        min_val = root.val
        second_min = float('inf')

        def dfs(node: TreeNode | None):
            nonlocal second_min
            if not node:
                return

            if min_val < node.val < second_min:
                second_min = node.val
                return

            if node.val == min_val:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return second_min if second_min < float('inf') else -1
