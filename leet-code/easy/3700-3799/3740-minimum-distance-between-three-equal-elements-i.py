# You are given an integer array nums.
#
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
#
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i), where abs(x) denotes the absolute value of x.
#
# Return an integer denoting the minimum possible distance of a good tuple. If no good tuples exist, return -1.

from collections import defaultdict
from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        result = float('inf')

        for i, num in enumerate(nums):
            positions[num].append(i)

            if len(positions[num]) >= 3:
                result = min(result, 2 * (i - positions[num][-3]))

        return result if result != float('inf') else -1
