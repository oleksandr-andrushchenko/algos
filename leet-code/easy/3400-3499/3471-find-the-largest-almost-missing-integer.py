# You are given an integer array nums and an integer k.
#
# An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
#
# Return the largest almost missing integer from nums. If no such integer exists, return -1.
#
# A subarray is a contiguous sequence of elements within an array.


from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = Counter()

        for i in range(len(nums) - k + 1):
            counts.update(set(nums[i:i + k]))

        return max((num for num, count in counts.items() if count == 1), default=-1)
