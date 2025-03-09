# 🔹 1. Sliding Window

# 📌 Pattern Explanation:
# Used when solving problems with contiguous subarrays or substrings.
# Helps optimize brute-force O(N²) to O(N).

# 📌 Concept:
# Maintain a "window" (a subarray or substring) that satisfies a condition.
# Expand or contract the window dynamically.

# 📌 Popular Problems:
# Maximum Sum Subarray of Size K
# Longest Substring Without Repeating Characters
# Longest Substring with K Distinct Characters
# Minimum Window Substring
# Longest Repeating Character Replacement
# Permutation in String
# Find All Anagrams in a String
# Smallest Subarray with Sum ≥ K

# ✅ What is it?
# Sliding Window is an efficient way to solve subarray problems by keeping a "window" (subarray) and expanding/shrinking it dynamically.
#
# ✅ When to Use?
# ✔️ Finding longest/shortest subarrays
# ✔️ Substring problems (e.g., longest unique substring)
# ✔️ Subarray sum problems

# 📌 Example 2: Longest Substring Without Repeating Characters
# 👉 Find the length of the longest substring in s where all characters are unique.

# ✅ Sliding Window Technique (Essence)
# 💡 Concept: Instead of recalculating everything, "slide" a window over the array dynamically.
#
# Expands when we haven't met the condition.
# Shrinks when we've exceeded the condition.
# Optimizes brute force (O(N²) → O(N)) by avoiding redundant calculations.
# 🛠 When to Use?
# ✔️ Finding subarrays/substrings (e.g., Longest Substring Without Repeating Characters)
# ✔️ Optimizing contiguous sum problems
# ✔️ Problems involving ranges, frequency counting, or min/max constraints

# s = "abcabcbbqwert" -> len("bqwert")
s = "abcabcbbqwert"
expected = 6


# O(N) and O(N)
def longest_unique_substring(s):
    left, max_len = 0, 0  # `left` is the start of the window, `max_len` stores the longest unique substring length
    chars = set()  # A set to keep track of unique characters in the current window

    for right in range(len(s)):  # Expand the window by moving `right` pointer
        while s[right] in chars:  # If the character at `right` is already in the set, shrink the window
            chars.remove(s[left])  # Remove the leftmost character to make space for the new one
            left += 1  # Move `left` pointer forward

        chars.add(s[right])  # Add the new character to the set
        max_len = max(max_len, right - left + 1)  # Update the maximum length of the substring

    return max_len  # Return the maximum found length


print(longest_unique_substring(s) == expected)


# O(N²) and O(N)
def longest_unique_substring_brute_force(s):
    max_len = 0

    for i in range(len(s)):
        chars = set()
        for j in range(i, len(s)):
            char = s[j]

            if char in chars:
                break

            chars.add(char)
            max_len = max(len(chars), max_len)

    return max_len


print(longest_unique_substring_brute_force(s) == expected)

# ✅ Problem 2: Max Consecutive Ones
# 👉 Given a binary array nums, return the maximum number of consecutive 1s.

nums = [1, 1, 0, 1, 1, 1, 1, 1]
expected = 5


# O(N) and O(1)
def max_consecutive_ones(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1  # Increase count if we see a '1'
            max_count = max(max_count, current_count)  # Update max if needed
        else:
            current_count = 0  # Reset count when encountering '0'

    return max_count


print(max_consecutive_ones(nums) == expected)

# ✅ Problem 3: Smallest Subarray with Given Sum
# 👉 Given an array nums and a target S, find the smallest contiguous subarray whose sum is ≥ S.

nums = [2, 1, 5, 2, 3, 2]
S = 7
expected = 2


# O(N) and O(1)
def smallest_subarray_sum(nums, S):
    min_length = float('inf')  # Start with a very large value
    left = 0
    current_sum = 0

    for right in range(len(nums)):  # Expanding the window
        current_sum += nums[right]

        while current_sum >= S:  # Contract the window when condition is met
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]  # Shrink the window
            left += 1  # Move left pointer forward

    return 0 if min_length == float('inf') else min_length  # If no valid subarray found, return 0


print(smallest_subarray_sum(nums, S) == expected)

nums = [2, 1, 5, 2, 3, 2]
S = 7
expected = 2


def smallest_subarray_sum_brute_force(nums, S):
    min_length = float('inf')

    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            if cur_sum >= S:
                min_length = min(min_length, j - i + 1)
                break

    return 0 if min_length == float('inf') else min_length


print(smallest_subarray_sum_brute_force(nums, S) == expected)

# ✅ Problem 4: Longest Repeating Character Replacement
# 👉 Given a string s and an integer k, you can replace at most k characters to get the longest substring that contains only one repeating character.
from collections import defaultdict


# O(n) and O(1)
def character_replacement(s, k):
    char_count = defaultdict(int)
    left = max_freq = max_len = 0

    for right in range(len(s)):
        char_count[s[right]] += 1  # Add new character to the frequency map
        max_freq = max(max_freq, char_count[s[right]])  # Track most frequent char in window

        # Condition: If (window size - max frequency char) > k, shrink the window
        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1  # Remove leftmost character from window
            left += 1  # Move left pointer forward

        max_len = max(max_len, right - left + 1)  # Update max length found

    return max_len


# ✅ Problem 5: Maximum Sum Subarray of Size K
# 👉 Given an array nums and an integer k, find the maximum sum of any contiguous subarray of size k.

nums = [2, 1, 5, 1, 3, 2]
k = 3
expected = 9


# O(n) and O(1)
def max_sum_subarray(nums, k):
    if len(nums) < k:
        return 0  # Edge case: If k is larger than the array size

    window_sum = sum(nums[:k])  # Compute initial sum of first window
    max_sum = window_sum  # Set initial max sum

    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i + k]  # Slide window
        max_sum = max(max_sum, window_sum)  # Update max sum if needed

    return max_sum


print(max_sum_subarray(nums, k) == expected)


# O(nk) and O(1)
def max_sum_subarray_brute_force(nums, k):
    max_sum = float('-inf')  # Handle negative numbers

    for i in range(0, len(nums) - k + 1):  # ✅ Fix the loop range
        window_sum = sum(nums[i:i + k])  # ✅ Compute sum for the current window
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_sum_subarray_brute_force(nums, k) == expected)

# ✅ Problem 6: Longest Subarray with Ones after K Flips
# 👉 Given a binary array nums, you can flip at most k 0s into 1s. Find the longest contiguous subarray that contains only 1s.

nums = [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
k = 2
expected = 8


def longest_ones(nums, k):
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1  # Track the number of flipped 0s

        while zero_count > k:  # If flips exceed `k`, shrink window
            if nums[left] == 0:
                zero_count -= 1
            left += 1  # Move left pointer forward

        max_length = max(max_length, right - left + 1)  # Update max window size

    return max_length


print(longest_ones(nums, k) == expected)