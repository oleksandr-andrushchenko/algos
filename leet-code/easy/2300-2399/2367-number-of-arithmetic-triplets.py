# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is
# an arithmetic triplet if the following conditions are met:
#
# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        values = set(nums)
        count = 0

        for num in nums:
            if num + diff in values and num + 2 * diff in values:
                count += 1

        return count
