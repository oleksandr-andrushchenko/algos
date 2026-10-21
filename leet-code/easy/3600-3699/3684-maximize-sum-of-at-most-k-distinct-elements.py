# You are given a positive integer array nums and an integer k.
#
# Choose at most k elements from nums so that their sum is maximized. However, the chosen numbers must be distinct.
#
# Return an array containing the chosen numbers in strictly descending order.


from typing import List


class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(set(nums), reverse=True)[:k]
