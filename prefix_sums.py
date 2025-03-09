# Prefix Sum Pattern: Explanation and Key Concept

# The prefix sum technique is a common array manipulation strategy that helps to precompute cumulative sums efficiently.
# It allows quick retrieval of subarray sums and speeds up operations that would otherwise take O(N) per query down to O(1).


# prefix[i] = nums[0] + nums[1] + ... + nums[i]
# sum(L, R) = prefix[R] − prefix[L−1]


# Why Use Prefix Sum?
# Efficient Range Queries: It reduces repeated computations for range sums from O(N) to O(1).
# Optimizes Subarray Problems: Helps with counting subarrays with given properties.
# Works Well with Hash Maps: Used in problems like "Subarray Sum Equals K".


# 1. Range Sum Query - Immutable
# 📌 Problem: Given an integer array nums, precompute a structure to efficiently return the sum of elements between indices L and R.

class NumArray:
    def __init__(self, nums: list[int]):
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        self.prefix_sums = prefix_sums

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Test Cases
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
assert obj.sum_range(0, 2) == 1
assert obj.sum_range(2, 5) == -1
assert obj.sum_range(0, 5) == -3


# 2. Subarray Sum Equals K
# 📌 Problem: Count the number of subarrays whose sum equals k.

def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix_sum = 0
    prefix_counts = {0: 1}  # To handle cases where prefix_sum itself equals k

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum - k]  # Count subarrays that sum to k
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

    return count


# Test Cases
assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, 2, 3, 4, 5], 5) == 2
assert subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4


# 3. Find Pivot Index
# 📌 Problem: Find an index i where the sum of the left subarray equals the sum of the right subarray.

def pivot_index(nums: list[int]) -> int:
    l = len(nums)
    total_sum = sum(nums)

    prefix_sums = [0] * (l + 1)
    for i in range(l):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    for i in range(l):
        # left_sum = prefix_sums[i - 1 + 1] - prefix_sums[0]
        left_sum = prefix_sums[i]
        # todo: calculate just left_sum, no need to calculate prefix_sums
        # right_sum = prefix_sums[l] - prefix_sums[i + 1]
        # right_sum = prefix_sums[l] - prefix_sums[i] - nums[i]
        # right_sum = total_sum - prefix_sums[i] - nums[i]
        right_sum = total_sum - left_sum - nums[i]

        if left_sum == right_sum:
            return i

    return -1


# Test Cases
assert pivot_index([1, 7, 3, 6, 5, 6]) == 3
assert pivot_index([1, 2, 3]) == -1
assert pivot_index([2, 1, -1]) == 0


# 4. Minimum Size Subarray Sum
# 📌 Problem: Find the minimal length of a contiguous subarray where sum ≥ target.

def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    min_len = float('inf')  # Initialize to a large number
    cur_sum = 0  # Current sum in the window

    for right in range(len(nums)):
        cur_sum += nums[right]  # Expand window

        while cur_sum >= target:  # Try to shrink window
            min_len = min(min_len, right - left + 1)
            cur_sum -= nums[left]
            left += 1  # Move left pointer to shrink window

    return 0 if min_len == float('inf') else min_len  # Return 0 if no valid subarray exists


# Test Cases
assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
assert min_subarray_len(4, [1, 4, 4]) == 1
assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


# 5. Maximum Subarray Sum after One Removal
# 📌 Problem: Find the max sum of a subarray where at most one element can be removed.

def max_sum_after_one_removal(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]  # Only one element, no removal possible

    # Step 1: Compute max subarray sum ending at each index (Kadane’s forward)
    max_end = [0] * n
    max_end[0] = nums[0]
    for i in range(1, n):
        max_end[i] = max(nums[i], max_end[i - 1] + nums[i])

    # Step 2: Compute max subarray sum starting at each index (Kadane’s backward)
    max_start = [0] * n
    max_start[-1] = nums[-1]
    for i in range(n - 2, -1, -1):
        max_start[i] = max(nums[i], max_start[i + 1] + nums[i])

    # Step 3: Find the max sum without removal (normal Kadane result)
    max_sum_no_removal = max(max_end)

    # Step 4: Try removing one element and compute the max sum
    max_sum_with_removal = float('-inf')
    for i in range(1, n - 1):  # We cannot remove the first or last element
        max_sum_with_removal = max(max_sum_with_removal, max_end[i - 1] + max_start[i + 1])

    # Final result: Either we remove one element or take normal Kadane result
    return max(max_sum_no_removal, max_sum_with_removal)


# Test Cases
assert max_sum_after_one_removal([1, -2, 0, 3]) == 4
assert max_sum_after_one_removal([1, -1, -2, 2, 3, -1]) == 5
assert max_sum_after_one_removal([-1, -2, -3]) == -1


# 6. Count Subarrays with Even Sum
# 📌 Problem: Find the number of subarrays with an even sum.

def count_even_sum_subarrays(nums: list[int]) -> int:
    even_count, odd_count = 1, 0  # Initialize even prefix sum count as 1
    prefix_sum, count = 0, 0

    for num in nums:
        prefix_sum += num  # Compute running prefix sum

        if prefix_sum % 2 == 0:
            count += even_count  # Add all previous even prefix sums
            even_count += 1
        else:
            count += odd_count  # Add all previous odd prefix sums (as odd-odd=even)
            odd_count += 1

    return count


# Test Cases
assert count_even_sum_subarrays([1, 2, 3, 4]) == 4
assert count_even_sum_subarrays([2, 4, 6]) == 6
assert count_even_sum_subarrays([1, 3, 5]) == 0


# 7. Continuous Subarray Sum
# 📌 Problem: Find if there exists a subarray of size at least 2 that sums to a multiple of k

def check_subarray_sum(nums: list[int], k: int) -> bool:
    prefix_mod_map = {0: -1}  # Initialize with remainder 0 at index -1
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num  # Running sum

        if k != 0:
            prefix_sum %= k  # Modulo k to detect cycles

        if prefix_sum in prefix_mod_map:
            if i - prefix_mod_map[prefix_sum] > 1:  # Ensure at least 2 elements
                return True
        else:
            prefix_mod_map[prefix_sum] = i  # Store first occurrence of remainder

    return False


# Test Cases
assert check_subarray_sum([23, 2, 4, 6, 7], 6) == True
assert check_subarray_sum([23, 2, 6, 4, 7], 13) == False
assert check_subarray_sum([0, 0], 1) == True
