# You are given an integer array nums of length n, and an integer array queries of length m.
#
# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums
# such that the sum of its elements is less than or equal to queries[i].
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
# order of the remaining elements.

from typing import List
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix_sum = []

        current_sum = 0
        for num in nums:
            current_sum += num
            prefix_sum.append(current_sum)

        return [bisect_right(prefix_sum, query) for query in queries]
