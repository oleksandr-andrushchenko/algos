# You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the
# following conditions:
#
# 0 <= i < j < k < nums.length
# nums[i], nums[j], and nums[k] are pairwise distinct.
# In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
# Return the number of triplets that meet the conditions.

from typing import List
from collections import Counter


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        frequencies = Counter(nums)

        answer = 0
        left_count = 0
        remaining_count = len(nums)

        for frequency in frequencies.values():
            remaining_count -= frequency
            answer += left_count * frequency * remaining_count
            left_count += frequency

        return answer
