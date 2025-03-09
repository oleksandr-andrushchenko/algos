# What is a Tree?
# A tree is a hierarchical data structure consisting of nodes, where each node has a value and references to child nodes.
# It is commonly used for hierarchical relationships, such as file systems, organizational charts, and decision trees.

# Basic Terminology

# Node – A single element in a tree containing a value and pointers to its children.
# Root – The topmost node in a tree.
# Parent – A node that has children.
# Child – A node that is directly connected to another node when moving away from the root.
# Sibling – Nodes that share the same parent.
# Leaf Node – A node with no children.
# Depth – The number of edges from the root to a given node.
# Height – The number of edges on the longest path from a node to a leaf.

# Binary Tree – A tree in which each node has at most two children.
#         1
#        / \
#       2   3
#      / \
#     4   5

# Binary Search Tree (BST) – A binary tree where the left child is smaller, and the right child is greater than the parent.
#         8
#        / \
#       3   10
#      / \    \
#     1   6    14
#        / \   /
#       4   7 13
# Search: O(log N) in balanced BST
# Insert/Delete: O(log N) in balanced BST
# Worst Case (Skewed Tree): O(N)

# Balanced Tree – A tree where the height difference between left and right subtrees is minimal (e.g., AVL, Red-Black Tree).
# 1. AVL Tree
# A self-balancing BST where the height difference between left and right subtrees of every node is at most 1.
# Uses rotations to maintain balance.
# 2. Red-Black Tree
# A self-balancing BST with additional color properties (Red/Black).
# Guarantees O(log N) operations.
# 3. B-Trees
# Used in databases and filesystems.
# Can have multiple children per node, ensuring efficient disk access.

# Trie (Prefix Tree)
# A tree where each node represents a prefix.
# Commonly used in autocomplete, dictionary searches.

# Full Binary Tree – A binary tree where each node has either 0 or 2 children.
# Complete Binary Tree – A binary tree in which all levels are completely filled except possibly the last level, which is filled from left to right.
# Perfect Binary Tree – A binary tree where all leaf nodes are at the same depth, and every parent has exactly two children.


# Tree Traversal Methods
# Traversal means visiting each node in a tree systematically.

# 1. Depth-First Search (DFS)
# Explores as far down as possible before backtracking.

# 1.1. Inorder (LNR - Left, Node, Right): Left → Root → Right (Used in BSTs to get sorted order.)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")  # Process the node
        inorder(root.right)


def inorder_iterative(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val, end=" ")
        curr = curr.right


# 1.2. Preorder (NLR - Node, Left, Right): Root → Left → Right (Used to copy trees, create expressions.)
def preorder(root):
    if root:
        print(root.val, end=" ")  # Process the node
        preorder(root.left)
        preorder(root.right)


def preorder_iterative(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# 1.3. Postorder (LRN - Left, Right, Node): Left → Right → Root (Used to delete trees, evaluate expressions.)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")  # Process the node


def postorder_iterative(root):
    if not root:
        return
    stack = [root]
    output = []
    while stack:
        node = stack.pop()
        output.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print(" ".join(map(str, output[::-1])))


# 2. Breadth-First Search (BFS) / Level Order Traversal
# Visits all nodes at each level before moving to the next level.
# Uses a queue (FIFO).

from collections import deque


def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root):
    if not root:
        return -1
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)


def is_balanced(root):
    def height(root):
        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) >= 0


# Lowest Common Ancestor
def lcu(root, p, q):
    if not root:
        return None
    if root.val > p.val and root.val > q.val:
        return lcu(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lcu(root.right, p, q)
    return root


root_node = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))


# Breadth-First Search (BFS) - Level Order Traversal

#         1
#       /   \
#      2     3
#     / \   /
#   4    5 6

# Output: 1 2 3 4 5 6


def bfs(root):
    """
    node:  queue:
    1       2, 3
    2       3, 4, 5
    3       4, 5, 6
    4       5, 6
    5       6
    6

    :param root:
    :return:
    """
    if not root:
        return

    queue = deque([root])  # Initialize queue with root

    while queue:
        node = queue.popleft()  # Dequeue front element

        print(node.val, end=" ")  # Process the node

        if node.left:  # Enqueue left child if exists
            queue.append(node.left)
        if node.right:  # Enqueue right child if exists
            queue.append(node.right)


bfs(root_node)
print()


# Depth-First Search (DFS) - Preorder Traversal (Using Stack)
# Preorder (NLR - Node, Left, Right): Root → Left → Right (Used to copy trees, create expressions.)

#         1
#       /   \
#      2     3
#     / \   /
#   4    5 6

# Output: 1 2 4 5 3 6

def dfs_preorder(root):
    """
    node:  stack:
    1       3, 2
    2       3, 5, 4
    4       3, 5
    5       3
    3       6
    6

    :param root:
    :return:
    """
    if not root:
        return

    stack = [root]  # Initialize stack with root

    while stack:
        node = stack.pop()  # Pop from stack

        print(node.val, end=" ")  # Process the node

        # Push right child first, so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


dfs_preorder(root_node)
print()


# Depth-First Search (DFS) - Inorder Traversal (Using Stack)
# Inorder (LNR - Left, Node, Right): Left → Root → Right (Used in BSTs to get sorted order.)

#         1
#       /   \
#      2     3
#     / \   /
#   4    5 6

# Output: 4 2 5 1 3 6

def dfs_inorder(root):
    """
    node:  current:    stack:
            1
                        1, 2, 4
    4       -            1, 2
    2        5            1
                        1, 5
    5        -          1
    1        3          -
                        3, 6
    6        -          3
    3        -          -

    :param root:
    :return:
    """
    stack = []
    current = root

    while stack or current:
        while current:  # Push all left nodes
            stack.append(current)
            current = current.left

        node = stack.pop()  # Process the node
        print(node.val, end=" ")

        current = node.right  # Move to right child


dfs_inorder(root_node)
print()


# Depth-First Search (DFS) - Postorder Traversal (Using Stack)
# Postorder (LRN - Left, Right, Node): Left → Right → Root (Used to delete trees, evaluate expressions.)

#         1
#       /   \
#      2     3
#     / \   /
#   4    5 6

# Output: 4 5 2 6 3 1

def dfs_postorder(root):
    if not root:
        return

    stack = [root]
    nodes = []

    while stack:
        node = stack.pop()
        nodes.append(node)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    while nodes:
        node = nodes.pop()  # Process the node
        print(node.val, end=" ")


dfs_postorder(root_node)
print()
