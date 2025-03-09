# 🔹 5. Top K Elements (Heap)

# 📌 Pattern Explanation:
# Used to find the Kth smallest/largest elements efficiently.

# 📌 Concept:
# Uses Min-Heap (default) or Max-Heap (negative values).

# 📌 Popular Problems:
# Kth Largest Element in an Array
# Top K Frequent Elements
# K Closest Numbers
# Find the Median from Data Stream
# Merge K Sorted Lists
# Smallest Range Covering Elements from K Lists


# A heap is a binary tree-based data structure that follows the heap property:
#
# Min-Heap: The parent node is always smaller than its child nodes.
# Max-Heap: The parent node is always larger than its child nodes.


import heapq

# 🔹 Why Use Heaps?
# Efficiently find the min/max element → O(1) for retrieval.
# Efficient insertion and deletion → O(log N).
# Used for priority queues, sorting, and top K elements problems.

#
# Operation	Min-Heap Example	Max-Heap Example
# Insert (O(log N))	Insert and bubble up	Insert and bubble up
# Get Min/Max (O(1))	Root is the min	Root is the max
# Remove Min/Max (O(log N))	Remove root, bubble down	Remove root, bubble down
# Heapify an Array (O(N))	Convert array to heap	Convert array to heap

# 1️⃣ Insert an Element (O(log N))
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
heapq.heappush(heap, 11)
heapq.heappush(heap, 3)

print(heap)  # [1, 7, 2, 10, 11, 3]

# 2️⃣ Remove the Smallest Element (O(log N))

print(heapq.heappop(heap))  # 1
print(heap)  # [2, 7, 3, 10, 11]

# 3️⃣ Get the Smallest Element Without Removing (O(1))

print(heap[0])  # 2

# 4️⃣ Convert a List into a Min-Heap (O(N))

nums = [1, 5, 8, 9, 2, 4, 5, 6, 7]
heapq.heapify(nums)
print(nums)  # [1, 2, 4, 6, 5, 8, 5, 9, 7]

# 5️⃣ Max-Heap Using heapq (Simulated)
# Since Python’s heapq is a Min-Heap, we can simulate a Max-Heap by storing negative values.

max_heap = []
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -15)

print(-heapq.heappop(max_heap))  # Output: 15 (Largest value)


# 🔹 Top K Elements Pattern
# The Top K Elements pattern is commonly used when solving problems related to finding the K largest, smallest, or most frequent elements in an array

# 🔹 When to Use This Pattern?

# Find the K largest or smallest elements in an array.
# Find the K most frequent elements.
# Find the median of a running stream of numbers.
# Find the K closest numbers to a target.


# 🔹 Common Techniques

# 1. Min-Heap (Priority Queue) Approach
# Use a Min-Heap (O(N log K)) to store the top K elements efficiently.
# Works well when N is large and K is small.
# Only maintain K elements in the heap.

# 2. Sorting Approach (O(N log N))
# Sort the array and take the top or bottom K elements.
# Slower but simpler than heaps.

# 3. QuickSelect Algorithm (O(N) on average)
# A variation of QuickSort.
# Used for Kth largest/smallest elements.


# 1. Kth Largest Element in an Array
# 📌 Problem: Find the Kth largest element in an unsorted array.


def kth_largest(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


print(kth_largest([3, 2, 1, 5, 6, 4], 2) == 5)
print(kth_largest([7, 10, 4, 3, 20, 15], 3) == 10)


# 2. Kth Smallest Element in an Array
# 📌 Problem: Find the Kth smallest element in an unsorted array.


def kth_smallest(nums: list[int], k: int) -> int:
    return heapq.nsmallest(k, nums)[-1]  # Returns the Kth smallest element


print(kth_smallest([3, 2, 1, 5, 6, 4], 2) == 2)
print(kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7)

# 3. Top K Frequent Elements
# 📌 Problem: Given a list of numbers, return the K most frequent elements.

from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.get)


print(top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
print(top_k_frequent([4, 4, 4, 4, 5, 5, 5, 2, 2, 3, 3, 3], 3) == [4, 5, 3])


# 4. K Closest Numbers to Target
# 📌 Problem: Find the K numbers closest to X in a sorted array.

def k_closest_numbers(nums: list[int], k: int, x: int) -> list[int]:
    return sorted(heapq.nsmallest(k, nums, key=lambda num: abs(num - x)))


print(k_closest_numbers([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4])
print(k_closest_numbers([1, 3, 7, 8, 9], 2, 5) == [3, 7])


# 5. Find the Median of a Running Stream
# 📌 Problem: Implement a class that supports adding numbers and finding the median.

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap

    def add_num(self, num: int):
        heapq.heappush(self.small, -num)  # Insert into max heap
        heapq.heappush(self.large, -heapq.heappop(self.small))  # Balance heaps

        if len(self.small) < len(self.large):  # Ensure small heap has equal/more elements
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0  # Median of two middle elements


# Test Cases
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median() == 1.5)
mf.add_num(3)
print(mf.find_median() == 2)
