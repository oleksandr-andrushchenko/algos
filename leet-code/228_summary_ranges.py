# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        start = nums[0]

        def calc(curr):
            if start == curr:
                res.append(str(start))
            else:
                res.append(f"{start}->{curr}")

        for i in range(len(nums) - 1):
            cur = nums[i]
            nxt = nums[i + 1]
            if nxt != cur + 1:
                calc(cur)
                start = nxt

        # handle last range
        calc(nums[-1])

        return res
