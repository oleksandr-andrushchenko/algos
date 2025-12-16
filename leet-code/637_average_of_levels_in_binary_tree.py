# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_count)

        return result
