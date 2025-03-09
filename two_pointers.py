# ✅ What is it?
# Two Pointers is an optimized approach that uses two indices (pointers) to process an array from both ends or within a subrange.
#
# ✅ When to Use?
# ✔️ Searching for pairs (e.g., sum problems)
# ✔️ Reversing an array in-place
# ✔️ Merging two sorted arrays
# ✔️ Removing duplicates from a sorted array
from os import remove


# ✅ Two Pointers Technique (Essence)
# 💡 Concept: Use two moving pointers to process an array efficiently.
#
# One pointer starts from the left, the other from the right (or both move within a subrange).
# Optimizes nested loops (O(N²) → O(N)) by eliminating unnecessary checks.
# 🛠 When to Use?
# ✔️ Searching for pairs (e.g., Two Sum, Remove Duplicates)
# ✔️ Sorting-based problems (e.g., Merge Sorted Arrays)
# ✔️ Finding boundaries or merging elements


# Example: nums = [1, 2, 3, 4, 6, 8], target = 10

# Step 1: Start with left = 0 and right = 5
# nums = [1, 2, 3, 4, 6, 8]
#         ↑              ↑
#       left           right

# Step 2: Move left → left = 1
# nums = [1, 2, 3, 4, 6, 8]
#            ↑        ↑
#          left     right


# 📌 Example 1: Two Sum (Sorted Array)
# 👉 Given a sorted array nums and a target t, return indices of two numbers that add up to t.

# O(n) and O(1)
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        sum = nums[left] + nums[right]
        if sum == target:
            return (left, right)
        elif sum > target:
            right -= 1
        else:
            left += 1

    return -1


nums = [1, 4, 7, 9, 20, 23]
target = 27
expected = (1, 5)

print(two_sum_sorted(nums, target) == expected)


# O(n²) and O(1)
def two_sum_sorted_brute_force(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return -1


def two_sum_unsorted_hash_map(nums, target):
    num_to_idx = {}

    for i in range(0, len(nums)):
        num = nums[i]
        complement = target - num

        if complement in num_to_idx:
            return (num_to_idx[complement], i)

        num_to_idx[num] = i

    return -1


nums = [1, 20, 7, 9, 4, 23]
target = 27
expected = (1, 2)

# i                 0           1           2
# current_num       1           20          7: return (1,2)
# current_diff      26          7
# visited_diffs     {26:0}      {26:0,7:1}

# should be (1, 2)

print(two_sum_unsorted_hash_map(nums, target) == expected)

# Problem 1: Remove Duplicates from Sorted Array
# 👉 Given a sorted array nums, remove duplicates in-place so that each element appears only once.


nums = [1, 4, 4, 8, 13, 18, 18, 20, 20]
expected = [1, 4, 8, 13, 18, 20]


# O(N) and O(1)
def remove_duplicates(nums):
    if not nums:
        return 0

    unique_index = 0  # This keeps track of the position for unique elements

    for i in range(1, len(nums)):  # Start from 1 since first element is always unique
        if nums[i] != nums[unique_index]:  # If a new unique element is found
            unique_index += 1
            nums[unique_index] = nums[i]  # Move it to the next position

    return nums[:unique_index + 1]  # Unique elements


print(remove_duplicates(nums) == expected)


# O(N) and O(N)
def remove_duplicates_brute_force(nums):
    seen = set()
    unique_nums = []

    for num in nums:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)

    return unique_nums


print(remove_duplicates_brute_force(nums) == expected)

# ✅ Problem 1: Move Zeros
# 👉 Given an array nums, move all 0s to the end while maintaining the relative order of the other elements. Do this in-place.

nums = [1, 0, 5, 0, 0, 6, 7, 0]
expected = [1, 5, 6, 7, 0, 0, 0, 0]


#   right   nums                        left
#   0       [1, 0, 5, 0, 0, 6, 7, 0]    1
#   1       [1, 0, 5, 0, 0, 6, 7, 0]    1
#   2       [1, 5, 0, 0, 0, 6, 7, 0]    2
#   3       [1, 5, 0, 0, 0, 6, 7, 0]    2
#   4       [1, 5, 0, 0, 0, 6, 7, 0]    2
#   5       [1, 5, 6, 0, 0, 0, 7, 0]    3
#   6       [1, 5, 6, 7, 0, 0, 0, 0]    4

# O(N) and O(1)
def move_zeros(nums):
    # zero position to replace
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

    return nums


print(move_zeros(nums) == expected)

# ✅ Problem 2: Reverse a String (In-Place)
# 👉 Given a string s, reverse it in-place using Two Pointers (Modify s list directly).

s = 'qwrwqe'
expected = 'eqwrwq'


def reverse_string(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return ''.join(s)


print(reverse_string(s) == expected)

# ✅ Problem 3: Three Sum
# 👉 Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0.

nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1, -1, 2], [-1, 0, 1]]


# O(n²) and O(K), K - number of unique triples
def three_sum(nums):
    nums.sort()  # Sorting takes O(N log N)
    res = []

    for i in range(len(nums) - 2):  # Fixing one element at a time (O(N))
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:  # Two-pointer search (O(N))
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Move left & right to avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


print(three_sum(nums) == expected)

nums = [-1, 0, 1, 2, -1, -4]
expected = [(-1, 0, 1), (-1, -1, 2)]


# O(N^3) and O(1)
def three_sum_brute_force(nums):
    res = set()  # Use a set to avoid duplicates
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))  # Avoid duplicate triplets

    return list(res)  # Convert set back to list


print(three_sum_brute_force(nums) == expected)

nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1, 2, -1], [-1, 1, 0]]


# O(N^2) and O(N)
def three_sum_hash_set(nums):
    nums.sort()
    res = set()

    for i in range(len(nums) - 2):
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add((nums[i], nums[j], complement))
            seen.add(nums[j])  # Store visited numbers

    return list(map(list, res))


print(three_sum_hash_set(nums) == expected)

nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1, 0, 1], [-1, -1, 2]]


# O(N^2) and O(N)
def three_sum_hash_map(nums):
    res = set()

    for i in range(len(nums) - 2):
        seen = {}
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.add(tuple(sorted((nums[i], nums[j], complement))))
            seen[nums[j]] = j  # Store the index of nums[j]

    return list(map(list, res))


print(three_sum_hash_map(nums) == expected)


# 🔹 Two Pointers Technique: Key Concepts

# 💡Two pointers move towards each other
# Example: Finding pairs in a sorted array
# Left pointer (L) starts from the beginning, and Right pointer (R) starts from the end.
# They move towards each other based on conditions.

# 💡Two pointers move in the same direction (Sliding Window)
# Example: Finding a subarray with a given sum
# One pointer expands the window, and another shrinks it when needed.

# 💡Fast-Slow Pointer Approach
# Example: Detecting cycles in a linked list
# One pointer moves one step at a time, while the other moves two steps.


# 🔹 Popular Two Pointers Problems

# 1. Two Sum (Sorted Array)
# 📌 Problem: Given a sorted array nums, find two numbers that sum to target.
# 💡 Approach: Use two pointers (L at the start, R at the end).


def two_sum_sorted(nums: list[int], target: int) -> tuple:
    left, right = 0, len(nums) - 1

    while left < right:
        cur_sum = nums[left] + nums[right]

        if cur_sum == target:
            return (left, right)

        if cur_sum > target:
            right -= 1
        else:
            left += 1

    return ()


print(two_sum_sorted([1, 2, 3, 4, 6], 6) == (1, 3))
print(two_sum_sorted([2, 3, 7, 11, 15], 9) == (0, 2))
print(two_sum_sorted([1, 5, 8, 12], 20) == (2, 3))
print(two_sum_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 17) == (6, 9))
print(two_sum_sorted([-3, 1, 2, 4, 8], 5) == (1, 3))


# 2. Remove Duplicates from Sorted Array
# 📌 Problem: Given a sorted array, remove duplicates in-place and return the new length.

def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    left = 0  # Pointer for unique elements

    for right in range(1, len(nums)):
        if nums[right] != nums[left]:  # Found a new unique number
            left += 1  # Move `left` forward
            nums[left] = nums[right]  # Overwrite with the new unique number

    return left + 1  # Number of unique elements


nums1 = [1, 1, 2, 3, 3, 4]
print(remove_duplicates(nums1) == 4)

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(remove_duplicates(nums2) == 5)


# 3. Move Zeroes to End
# 📌 Problem: Move all zeroes in an array to the end, maintaining the order of non-zero elements.


def move_zeroes(nums: list[int]) -> None:
    left = 0  # Position for the next nonzero element

    for right in range(len(nums)):  # Start from index 0
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]  # Swap
            left += 1  # Move left pointer to track the next zero


nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1 == [1, 3, 12, 0, 0])

nums2 = [0, 0, 1]
move_zeroes(nums2)
print(nums2 == [1, 0, 0])


# 4. Valid Palindrome
# 📌 Problem: Given a string, determine if it is a palindrome considering only alphanumeric characters.

def is_palindrome(s: str) -> bool:
    # Implement two-pointer approach

    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Test Cases
print(is_palindrome("A man, a plan, a canal: Panama") == True)
print(is_palindrome("race a car") == False)
print(is_palindrome(" ") == True)


# 5. Container With Most Water
# 📌 Problem: Find two vertical lines that hold the most water in a histogram-like array.


def max_area(heights: list[int]) -> int:
    # Implement two-pointer approach
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        cur_area = min(heights[left], heights[right]) * (right - left)
        max_area = max(max_area, cur_area)

        # Move the pointer with the smaller height
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return max_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
print(max_area([1, 1]) == 1)
print(max_area([4, 3, 2, 1, 4]) == 16)


# 6. Three Sum (Triplet Sum to Zero)
# 📌 Problem: Find all unique triplets (a, b, c) where a + b + c = 0.


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Sort the array (O(N log N))
    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
            continue

        left, right = i + 1, len(nums) - 1  # Two-pointer setup

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Skip duplicate values to avoid duplicate triplets
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:  # Need a larger sum
                left += 1
            else:  # Need a smaller sum
                right -= 1

    return res


print(three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(three_sum([0, 1, 1]) == [])
print(three_sum([0, 0, 0]) == [[0, 0, 0]])


# 7. Subarray Product Less Than K
# 📌 Problem: Find the number of contiguous subarrays where the product of all elements is less than k.


def num_subarray_product_less_than_k(nums: list[int], k: int) -> int:
    # Implement sliding window approach
    if k <= 1:  # Edge case where no valid subarrays can exist
        return 0

    left = 0
    product = 1
    count = 0

    for right in range(len(nums)):
        product *= nums[right]  # Expand window

        while product >= k:  # If product exceeds k, shrink window
            product /= nums[left]
            left += 1

        count += right - left + 1  # Count valid subarrays ending at `right`

    return count


print(num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8)
print(num_subarray_product_less_than_k([1, 2, 3], 0) == 0)
print(num_subarray_product_less_than_k([1, 1, 1], 2) == 6)


# 8. Longest Substring Without Repeating Characters
# 📌 Problem: Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s: str) -> int:
    # Implement sliding window approach
    max_len = 0
    seen = set()

    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_len = max(max_len, len(seen))

    return max_len


print(length_of_longest_substring("abcabcbb") == 3)
print(length_of_longest_substring("bbbbb") == 1)
print(length_of_longest_substring("pwwkew") == 3)

# 9. Minimum Window Substring
# 📌 Problem: Given strings s and t, find the minimum window substring in s that contains all characters in t.

from collections import Counter


def min_window(s: str, t: str) -> str:
    # Implement sliding window approach
    if not s or not t:
        return ""

    t_count = Counter(t)  # Frequency map of characters in `t`
    window_count = {}

    left, right = 0, 0
    required = len(t_count)  # Number of unique characters in `t`
    formed = 0  # Number of characters met in the current window
    min_length = float("inf")
    min_window = ""

    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1  # Character count matches the requirement

        while left <= right and formed == required:  # Valid window
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]

            # Shrink window from the left
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed -= 1  # No longer a valid window

            left += 1  # Move left pointer forward

        right += 1  # Expand the window

    return min_window


print(min_window("ADOBECODEBANC", "ABC") == "BANC")
print(min_window("a", "a") == "a")
print(min_window("a", "aa") == "")


# 10. Find the Duplicate Number
# 📌 Problem: Given an array nums containing n+1 integers where each integer is in the range [1, n], find the duplicate number.

def find_duplicate(nums: list[int]) -> int:
    # Step 1: Detect cycle using Floyd’s Tortoise and Hare
    slow, fast = nums[0], nums[nums[0]]

    while slow != fast:
        slow = nums[slow]  # Move slow by 1 step
        fast = nums[nums[fast]]  # Move fast by 2 steps

    # Step 2: Find the entrance to the cycle (duplicate number)
    slow = 0  # Reset slow to start
    while slow != fast:
        slow = nums[slow]  # Move slow by 1 step
        fast = nums[fast]  # Move fast by 1 step

    return slow  # The duplicate number


print(find_duplicate([1, 3, 4, 2, 2]) == 2)
print(find_duplicate([3, 1, 3, 4, 2]) == 3)
print(find_duplicate([1, 1]) == 1)


# 🔹 2. Two Pointers

# 📌 Pattern Explanation:
# Used when working with sorted arrays or linked lists.
# Helps solve problems efficiently by using two pointers moving towards each other.

# 📌 Concept:
# Place two pointers at opposite ends or same end but move differently.
# Adjust pointers based on conditions.

# 📌 Popular Problems:
# Two Sum (Sorted)
# Remove Duplicates from Sorted Array
# Valid Palindrome
# Container With Most Water
# Three Sum
# Trapping Rain Water
# Partition List
# Move Zeros to End