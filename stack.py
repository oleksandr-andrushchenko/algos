# A last-in, first-out (LIFO) structure where the last element added is removed first.

# Use cases: Function calls, backtracking, undo/redo, balanced parentheses
# Operations: push(), pop(), peek(), is_empty()

# 🔹 Key Techniques with Stacks

# ✅ 1. Valid Parentheses (Stack) → Checking balanced brackets
# ✅ 2. Min Stack (Stack) → A stack that supports retrieving the minimum element
# ✅ 3. Implement Queue Using Two Stacks (Stack) → Simulating queue behavior


class Stack:
    def __init__(self):
        self.stack = []

    # O(1)
    def push(self, value):
        self.stack.append(value)

    # O(1)
    def is_empty(self):
        return len(self.stack) == 0

    # O(1)
    def pop(self):
        return None if self.is_empty() else self.stack.pop()

    # O(1)
    def peek(self):
        return None if self.is_empty() else self.stack[-1]


# ✅ Problem 1: Valid Parentheses
# 👉 Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

# "(]{[" -> False
#   i   char    stack
#   0   "("     "("
#   1   "]"     False

# "]{" -> False

# "[{}]" -> True
#   i   char    stack
#   0   "["     "["
#   1   "{"     "[", "{"
#   2   "}"     "["
#   3   "]"     <empty>

# "[]{}" -> True

def is_valid_parentheses(s):
    stack = Stack()
    close_to_open = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # Close char
        if char in close_to_open:
            if stack.is_empty() or stack.pop() != close_to_open[char]:
                return False  # Mismatch or trying to pop from an empty stack
        # Open char
        else:
            stack.push(char)

    return stack.is_empty()  # Stack should be empty if valid


# ✅ Problem 2: Min Stack
# 👉 Design a stack that supports push(), pop(), top(), and get_min() in constant time.

class MinStack:
    def __init__(self):
        self.stack = []  # Normal stack
        self.min_stack = []  # Stack to track the minimum

    def push(self, x: int):
        self.stack.append(x)  # Push element onto the stack

        # Push onto min_stack only if it's the new minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            return None  # Stack is empty

        popped = self.stack.pop()

        # If the popped element is the minimum, remove it from min_stack
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None  # Return top element

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None  # Return min element


# ✅ Problem 3: Implement Queue Using Two Stacks
# 👉 Implement a queue using two stacks (one for enqueue, one for dequeue).

class MyQueue:
    # Implement this class
    pass


# ✅ Problem 1: Next Greater Element
# 👉 Given an array, find the next greater element for each element.
# 👉 If there is no greater element, return -1.

def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)  # Initialize result with -1

    for i in range(len(nums) - 1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= nums[i]:  # Pop smaller elements
            stack.pop()
        if stack:
            result[i] = stack[-1]  # Top of stack is the next greater element
        stack.append(nums[i])  # Push current element to stack

    return result


print(next_greater_element([4, 5, 2, 10, 8]))  # Expected: [5, 10, 10, -1, -1]
print(next_greater_element([1, 3, 2, 4]))  # Expected: [3, 4, 4, -1]
print(next_greater_element([6, 8, 0, 1, 3]))  # Expected: [8, -1, 1, 3, -1]
print(next_greater_element([10, 9, 8, 7]))  # Expected: [-1, -1, -1, -1]


# ✅ Problem 2: Largest Rectangle in Histogram
# 👉 Given an array of heights, find the largest rectangle that can be formed.

def largest_rectangle_area(heights):
    stack = []  # Stores (index, height)
    max_area = 0

    for i, h in enumerate(heights + [0]):  # Append 0 to handle remaining heights
        while stack and h < stack[-1][1]:  # Calculate max area for popped height
            index, height = stack.pop()
            width = i if not stack else i - stack[-1][0] - 1
            max_area = max(max_area, height * width)
        stack.append((i, h))

    return max_area


print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))  # Expected: 10
print(largest_rectangle_area([2, 4]))  # Expected: 4
print(largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]))  # Expected: 12
print(largest_rectangle_area([1, 2, 3, 4, 5]))  # Expected: 9


def largest_rectangle_brute_force(heights):
    max_area = 0

    for i in range(len(heights)):  # Pick starting bar
        min_height = heights[i]

        for j in range(i, len(heights)):  # Expand the rectangle
            min_height = min(min_height, heights[j])  # Limit height
            area = min_height * (j - i + 1)  # Width = (j - i + 1)
            max_area = max(max_area, area)

    return max_area
