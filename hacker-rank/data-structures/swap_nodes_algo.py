#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

from collections import deque


def swapNodes(indexes, queries):
    # Build nodes: node_index -> [left_child_or_None, right_child_or_None]
    nodes = {i + 1: [l if l != -1 else None, r if r != -1 else None]
             for i, (l, r) in enumerate(indexes)}

    result = []
    for k in queries:
        # BFS to swap children at depths multiple of k
        q = deque([(1, 1)])  # (node_index, depth)
        while q:
            node, depth = q.popleft()
            if node is None:
                continue
            if depth % k == 0:
                nodes[node][0], nodes[node][1] = nodes[node][1], nodes[node][0]
            left, right = nodes[node]
            if left: q.append((left, depth + 1))
            if right: q.append((right, depth + 1))

        # Iterative inorder traversal (stack-based, to avoid recursion limit)
        inorder_res = []
        stack = []
        curr = 1  # root index is always 1 per problem statement
        while stack or curr is not None:
            # go to leftmost node
            while curr is not None:
                stack.append(curr)
                curr = nodes[curr][0]
            # visit node
            curr = stack.pop()
            inorder_res.append(curr)
            # go to right subtree
            curr = nodes[curr][1]

        result.append(inorder_res)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
