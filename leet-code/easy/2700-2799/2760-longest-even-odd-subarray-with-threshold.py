# You are given a 0-indexed integer array nums and an integer threshold.
#
# Find the length of the longest subarray of nums starting at index l and ending at index r (0 <= l <= r < nums.length)
# that satisfies the following conditions:
#
# nums[l] % 2 == 0
# For all indices i in the range [l, r - 1], nums[i] % 2 != nums[i + 1] % 2
# For all indices i in the range [l, r], nums[i] <= threshold
# Return an integer denoting the length of the longest such subarray.
#
# Note: A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        answer = 0
        length = 0

        for i, num in enumerate(nums):
            if num > threshold:
                length = 0
            elif length == 0:
                if num % 2 == 0:
                    length = 1
            elif nums[i - 1] % 2 != num % 2:
                length += 1
            elif num % 2 == 0:
                length = 1
            else:
                length = 0

            answer = max(answer, length)

        return answer
