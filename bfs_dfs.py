# 🔹 7. DFS & BFS
from collections import deque
from typing import Optional, List


# 📌 Pattern Explanation:
# Used in graph and tree traversal.

# 📌 Concept:
# DFS recursively explores deeper nodes first.
# BFS explores all neighbors before going deeper.

# 📌 Popular Problems:
# Number of Islands
# Word Search
# Graph Traversal
# Clone Graph
# Rotting Oranges
# Pacific Atlantic Water Flow

class TreeNode:
    def __init__(self, val=Optional[None], left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 📌 1. Binary Tree Level Order Traversal (BFS)
# Problem: Given the root of a binary tree, return its level order traversal (each level's nodes from left to right).

# 1. Use Breadth-First Search (BFS).
# 2. Utilize a queue (FIFO) to process nodes level by level.
# 3. Extract all nodes from the current level, then enqueue their children.

#           1
#         /   \
#       2      3
#            /   \
#           4     5

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    📌 1. Binary Tree Level Order Traversal (BFS)

    Problem: Given the root of a binary tree, return its level order traversal
    (each level's nodes from left to right).

    - Uses Breadth-First Search (BFS).
    - Utilizes a queue (FIFO) to process nodes level by level.
    - Extracts all nodes from the current level, then enqueues their children.

    Example Tree:

            1
          /   \
        2      3
             /   \
            4     5

    Expected Output: [[1], [2, 3], [4, 5]]
    """

    levels = []  # Stores the result as a list of lists (each sublist represents a level)
    if not root:
        return levels  # Return empty list if tree is empty

    queue = deque([root])  # Initialize queue with the root node

    while queue:
        level_size = len(queue)  # Number of nodes in the current level
        level_nodes = []  # List to store node values at this level

        # Process all nodes in the current level
        for _ in range(level_size):
            node = queue.popleft()  # Dequeue the front node
            level_nodes.append(node.val)  # Store its value

            # Enqueue left child if it exists
            if node.left:
                queue.append(node.left)

            # Enqueue right child if it exists
            if node.right:
                queue.append(node.right)

        levels.append(level_nodes)  # Add the current level nodes to the result

    return levels


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
assert level_order(root) == [[1], [2, 3], [4, 5]]

assert level_order(None) == []


# 📌 2. Validate Binary Search Tree (BST)
# Problem: Given a binary tree, determine if it is a valid Binary Search Tree (BST).

# Inorder Traversal (DFS)
# If you traverse BST inorder, it should be strictly increasing.
# Recursive Approach
# Use a min-max range to validate nodes.

def is_valid_bst(root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if not root:
        return True

    # The node must be in the valid range (min_val, max_val)
    if not (min_val < root.val < max_val):
        return False

    # Recursively validate left subtree and right subtree
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)


root1 = TreeNode(2, TreeNode(1), TreeNode(3))
assert is_valid_bst(root1) == True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
assert is_valid_bst(root2) == False


# 📌 3. Lowest Common Ancestor (LCA) of a Binary Tree
# Problem: Find the lowest common ancestor (LCA) of two given nodes in a binary tree.

# Recursive DFS
# If p and q are on different sides, return root.
# If both are in left or right subtree, recurse accordingly.

# O(log N) (if the tree is balanced), O(N) (if skewed).
# O(K)
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root:  # Edge case: Empty tree
        return None

    # If both p and q are in the left subtree, recurse left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # If both p and q are in the right subtree, recurse right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Otherwise, we have found the LCA
    return root


# O(log N) (if the tree is balanced), O(N) (if skewed).
# O(1)
def lowest_common_ancestor_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left  # Move left
        elif p.val > root.val and q.val > root.val:
            root = root.right  # Move right
        else:
            return root  # Found the split point (LCA)
    return None  # Should never reach here in a valid BST


root = TreeNode(3,
                TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode(0), TreeNode(8)))

p, q = root.left, root.right  # Nodes 5 and 1
assert lowest_common_ancestor(root, p, q).val == 3


# p, q = root.left, root.left.right.right  # Nodes 5 and 4
# assert lowest_common_ancestor(root, p, q).val == 5


# 📌 4. Serialize and Deserialize a Binary Tree
# Problem: Convert a binary tree to a string and back.

# BFS (Level Order) Serialization
# Use a queue and process nodes in order.
# BFS Deserialization
# Use splitting and reconstruction.

#                       1
#                     /   \
#                    2     3
#                        /   \
#                      4      5

# serialized:       1,2,3,,,4,5

def serialize(root: Optional[TreeNode]) -> str:
    if not root:
        return 'null'

    serialized = []

    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node:
            serialized.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            serialized.append('null')

    # Remove trailing "null" values to keep output minimal
    while serialized and serialized[-1] == "null":
        serialized.pop()

    return ','.join(serialized)


def deserialize(data: str) -> Optional[TreeNode]:
    if data == 'null' or not data:
        return None

    values = data.split(',')
    root = TreeNode(int(values[0]))
    i = 1

    queue = deque([root])
    while queue and i < len(values):
        node = queue.popleft()

        if values[i] != 'null':
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != 'null':
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
data = serialize(root)
assert deserialize(data).val == root.val


# 📌 5. Binary Tree Right Side View
# Problem: Return the rightmost node at each level of a tree.

# Use BFS (Level Order)
# Only take the last node from each level.

def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    📌 5. Binary Tree Right Side View

    Problem: Return the rightmost node at each level of a tree.

    - Uses Breadth-First Search (BFS) (Level Order Traversal).
    - Only takes the last node from each level.

    Example Tree:

            1
          /   \
        2      3
         \       \
          5       4

    Expected Output: [1, 3, 4]
    """

    right_side = []  # Stores the rightmost nodes at each level
    if not root:
        return right_side  # Return empty list if tree is empty

    queue = deque([root])  # Initialize queue with the root node

    while queue:
        level_size = len(queue)  # Number of nodes in the current level

        for i in range(level_size):
            node = queue.popleft()  # Dequeue the front node

            # If this is the last node of the level, add it to result
            if i == level_size - 1:
                right_side.append(node.val)

            # Add children to queue for next level traversal
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return right_side  # Returns the rightmost nodes from each level


root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
assert right_side_view(root) == [1, 3, 4]


# 📌 6. Number of Islands (Graph DFS/BFS)
# Problem: Given a 2D grid where '1' represents land and '0' represents water, count the number of islands.

# Use DFS or BFS to traverse connected components.
# Change visited land to "0" to avoid revisits.

def num_islands(grid: List[List[str]]) -> int:
    """
    📌 Number of Islands (DFS Approach)

    - Given a grid of '1's (land) and '0's (water), count the number of islands.
    - An island is a group of adjacent '1's connected horizontally or vertically.
    - The function modifies the grid in place to mark visited cells.

    Example Grid:

    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    Expected Output: 3
    """

    if not grid or not grid[0]:  # ✅ Corrected base case
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0  # Number of islands

    def mark(i: int, j: int):
        """Perform DFS to mark all connected '1's as visited."""
        # Check if out of bounds or already visited
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
            return

        grid[i][j] = '0'  # Mark as visited

        # Explore all 4 directions (Up, Down, Left, Right)
        mark(i - 1, j)  # Up
        mark(i + 1, j)  # Down
        mark(i, j - 1)  # Left
        mark(i, j + 1)  # Right

    # Iterate through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':  # Found an island
                count += 1
                mark(i, j)  # Perform DFS to mark all connected land

    return count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
assert num_islands(grid) == 1

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
assert num_islands(grid) == 3


# 📌 7. Clone Graph
# Problem: Given a reference of a node in a connected undirected graph, return a deep copy.

# Keep track of cloned nodes to avoid cycles.
# Traverse and clone recursively.

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Node) -> Node:
    pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned_graph = clone_graph(node1)
assert cloned_graph.val == 1
assert len(cloned_graph.neighbors) == 2
