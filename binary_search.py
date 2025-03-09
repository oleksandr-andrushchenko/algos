# 🔹 6. Binary Search

# 📌 Pattern Explanation:
# Used for searching efficiently in sorted data structures.

# 📌 Concept:
# Reduce the search space by half at each step.

# 📌 Popular Problems:
# Binary Search
# Search in Rotated Sorted Array
# Find Minimum in Rotated Sorted Array
# Find Peak Element
# Koko Eating Bananas
# Median of Two Sorted Arrays

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


nums = [1, 3, 8, 15, 17, 30, 33]
target = 17
expected = 4

print(binary_search(nums, target) == expected)
