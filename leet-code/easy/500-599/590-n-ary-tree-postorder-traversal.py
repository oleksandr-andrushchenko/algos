# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)

class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return []

        result = []

        def dfs(node: 'Node'):
            for child in node.children or []:
                dfs(child)
            result.append(node.val)

        dfs(root)
        return result
