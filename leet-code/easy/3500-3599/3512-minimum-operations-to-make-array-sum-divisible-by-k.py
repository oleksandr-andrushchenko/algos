# You are given an integer array nums and an integer k. You can perform the following operation any number of times:
#
# Select an index i and replace nums[i] with nums[i] - 1.
# Return the minimum number of operations required to make the sum of the array divisible by k.


from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
