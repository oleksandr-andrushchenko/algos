# You are given a sorted integer array nums and an integer k.
#
# Return an array such that each distinct element appears at most k times, while preserving the relative order of the
# elements in nums.
#
# Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        if k <= 0:
            return []

        result = []

        for num in nums:
            if len(result) < k or result[-k] != num:
                result.append(num)

        return result
