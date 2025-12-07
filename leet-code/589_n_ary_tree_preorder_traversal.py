# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)


class Node:
    def __init__(self, val: int | None = None, children: list['Node'] | None = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        result = []

        def dfs(node: 'Node'):
            if not node:
                return

            result.append(node.val)

            if node.children:
                for child in node.children:
                    dfs(child)

        dfs(root)
        return result
